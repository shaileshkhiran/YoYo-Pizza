import random
import json

import torch


import sqlite3 as sql
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Yo-Bot"

conn = sql.connect('Pizza.db')
cur = conn.cursor()
cur.execute('''create table if not exists orders(name text primary key, ph_no text not null, postal_code text not null,pizza_type text not null,pizza_size text not null,pizza_crust text not null)''')


details = {"name":None, "ph_no":None, "postal_code":None, "pizza_type":None, "pizza_size":None, "pizza_crust":None, }
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    sent = sentence
    if sentence == "quit":
        print(f"{bot_name}: Thanks for using the {bot_name} bot, see ya later.")
        break
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    # print(tags[predicted.item()])
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                # DB QUERIES
                print(f"{bot_name}: {random.choice(intent['responses'])}")
                if tag == "pizza_type":
                    details.update({"pizza_type": sent})
                elif tag == "pizza_size":
                    details.update({"pizza_size":sent})
                elif tag == "pizza_crust":
                    details.update({"pizza_crust":sent})
                elif tag == "user_particulars":
                    sent = input("You:")
                    particulars = sent.split(" ")
                    details.update({"name":particulars[0]})
                    # Check if number is 10 digits, use particulars[2] for checking
                    if len(str(particulars[1])) == 10:
                        details.update({"ph_no":str(particulars[1])})
                    else:
                        print(f"{bot_name}: Phone numbers are 10 digit long. Please try again. Press Ok to retry.")
                    # Check if number is 6 digits, use particulars[2] for checking
                    if len(str(particulars[2])) == 6:
                        details.update({"postal_code":str(particulars[2])})
                    else:
                        print(f"{bot_name}: Postal Codes are 6 digit long. Please try again. Press Ok to retry.")
                        continue
                    print(f"{bot_name}: I got your details. Updating...\n")

                count = 0
                for i in details.values():
                    if i != None:
                        count+=1
                        # print(type(i))
                        # print("")
                if count == 6:
                    cur.execute(f'insert into orders values {tuple(details.values())}')
                    print(f"{bot_name}: Your order has been recorded.")
                    cur.execute('''select * from orders''')
                    print("DB Returns ( Just for development purposes ):\n")
                    print(cur.fetchall())
                    conn.commit()



    else:
        print(f"{bot_name}: I do not understand...")
