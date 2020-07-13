#import libraries
import smtplib
import json
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#open json file to get sender and receiver details
with open("sample_json.JSON") as f:
    data = json.load(f) #load all content of json file into data variable
sender=data['sender'] #sender email-id is fetched from the json file
pwd=input("enter password for "+sender+" :")
#create SMPTP session
mail = smtplib.SMTP('smtp.gmail.com',587) #we are setting smtp for gmail, you can change the parameters depending upon which mail service you intend to use. The second parameter corresponds to the port.
mail.ehlo()
mail.starttls() #to enable TLS (security)
mail.login(sender,pwd) #to login into your emailid using your credentials
rec=data['receivers'] #to get details about receivers from the json file - their name and their emailid
m=MIMEMultipart() #creating instance of MIMEMultipart. It is used to set various attributes of an email such as sender,subject etc.
#function send_attachment - to read a file, give the file a name, encode it and attach it to the message to be sent.
def send_attachment(msg,m):
    m.attach(MIMEText(msg, 'plain')) #attaches the email body to m
    file_name = "test.pdf" #display name of the attachment(you can use any name you want). This name will appear in receiver's email
    path="<enter path here>" #path of the file to be attached
    attachment = open(path, "rb") #store contents of the path in attachment variable-which acts as the file handle
    #make an instance of MIMEBase
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p) #encode the file contents to base64
    #add payload header with filename
    p.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
    #attach instance p to instance m
    m.attach(p)
    mail.send_message(m) #final command to send the object m, which comprises of the whole message+attachment

for k,v in rec:
	#variable msg stores the body of the email.
	msg="hi "+k+", see the attachment!" #k is the name of receiver. This is done to personalise emails.
	m['Subject']="hello!" #to set subject of the mail
	m['From']=sender #to set the sender
	m['To']=v #v is the receiver email address
	send_attachment(msg,m) #function call
	msg="" # to reset for next iteration
	m=MIMEMultipart() #done to reset all object data for next iteration
mail.quit() #to end the smtp session
