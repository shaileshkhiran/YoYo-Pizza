# YoYo-Pizza

How to run

1. Through terminal, type python train.py - this runs the train data.
2. After it has run successfully , type python chat.py to run the chatbot.
3. Here the user must enter “I want a pizza” or just “pizza” , the bot replies with "Hi! what type of pizza do you want ?1.Hawaiian 2.Pepperoni 3.BBQ 4.Veggie".
If the user types anything other than the patterns , the bot replies “ I do not understand…”
4. The conversation is continued based on the same pattern-response format.
5. After all the details about the pizza are successfully gathered , the user is prompted to acknowledge with “Ok”.
6. Once the user types "Ok", the bot prompts the user to enter the user particulars i.e. Name, Phone Number, Postal code (Phone numbers must be 10 digit long and postal code must be 6 digit long). If not, the user is asked to type the user particulars again.
7. After successful validation of the user particulars, all the collected details are stored in a database.
8. The user can get the payment and delivery details by asking “Do you take credit cards?” and “How long does the delivery take?”.


