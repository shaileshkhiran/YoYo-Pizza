# YoYo-Pizza

How to run

1. Install all the required packages.
2. Through terminal, type python train.py - this runs the train data.
3. After it has run successfully , type python chat.py to run the chatbot.
4. Here the user must enter “I want a pizza” or just “pizza” , the bot replies with "Hi! what type of pizza do you want ?1.Hawaiian 2.Pepperoni 3.BBQ 4.Veggie".
5. If the user types anything other than the patterns , the bot replies “ I do not understand…”. 
6. The conversation is continued based on the same pattern-response format.
7. After all the details about the pizza are successfully gathered , the user is prompted to acknowledge with “Ok”.
8. Once the user types "Ok", the bot prompts the user to enter the user particulars i.e. Name, Phone Number, Postal code (Phone numbers must be 10 digit long and postal code must be 6 digit long). If not, the user is asked to type the user particulars again.
9. After successful validation of the user particulars, all the collected details are stored in a database.
10. The user can get the payment details by asking “Do you take credit cards?” and the delivery details by asking “How long does the delivery take?”.


