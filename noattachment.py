#import libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
#open json file to get sender and receiver details
with open("sample_json.JSON") as f:
    data = json.load(f) #load all content of json file into data variable
sender=data['sender'] #sender email-id is fetched from the json file
pwd=input("enter password for "+sender+" :")
#create SMTP session
mail = smtplib.SMTP('smtp.gmail.com',587) #we are setting smtp for gmail, you can change the attributes depending upon which mail service you intend to use. The second parameter corresponds to the port.
mail.ehlo()
mail.starttls() #to enable TLS (security)
mail.login(sender,pwd) #to login into your emailid using your credentials
rec=data['receivers'] #to get details about receivers from the json file - their name and their email-id
m = MIMEMultipart() #creating instance of MIMEMultipart. It is used to set various attributes of an email such as sender,subject etc.
for k,v in rec:
	#variable msg stores the body of the email.
	msg="hi "+k+" how are you?" #k is the name of receiver. This is done to personalise emails.
	m['Subject']="hello!" #to set subject of the mail
	m['From']=sender #to set the sender
	m['To']= v #v is the receiver email address
	m.attach(MIMEText(msg, 'plain')) #attaches the email body to m(instance of MIMEMultipart)
	mail.send_message(m) #final command to send the object m, which comprises of the message
	msg="" # to reset for next iteration
	m=MIMEMultipart() #done to reset all object data for next iteration
mail.quit() #to end the smtp session

