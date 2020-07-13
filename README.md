# Description
This is an email automation project which uses the smtplib module in python to send emails to multiple people simultaneously. It also allows sending an attachment along with the email. It reads a JSON file which stores a list of recipients. The use of JSON helps us to conveniently add several attributes such as name, address etc. associated with each recipient, thus making each email personalized and unique.

# Steps
1. set up a JSON file which contains a list of recipient email addresses along with the sender address. You can add additional attributes such as name, address, etc. associated with each recipient in a sub-list within the main receiver list. You can hence access each attribute of the sub-list to make each email personalized. Use the sample_json.JSON file for reference.
2. load this JSON file into the program
    -line 7 in noattachment.py
    -line 10 in withattachment.py
3. Use noattachment.py incase there is no attachment to be sent along with the email; else, use withattachment.py
4. You can write the message to be sent as a string stored in the 'msg' variable.
5. Incase you want to send an attachment along with the message, use withattachment.py. In this case, store the path of the file to be attached in the path variable (line 25).

