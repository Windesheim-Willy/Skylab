# import smtplib
# fromaddr = 'willythegarbagedisposal@gmail.com'
# toaddrs  = 's1096820@windesheim.nl'
# msg = 'Why,Oh why!'
# username = 'willythegarbagedisposal@gmail.com'
# password = 'Willy1234'
#
# msg = "\r\n".join([
#   "From: willythegarbagedisposal@gmail.com",
#   "To: s1096820@windesheim.nl",
#   "Subject: Testbericht",
#   "",
#   "Hierbij een testbericht van Willi. Groet, Marc"
#   ])
#
# server = smtplib.SMTP('smtp.gmail.com:587')
# server.ehlo()
# server.starttls()
# server.login(username,password)
# server.sendmail(fromaddr, toaddrs, msg)
# server.quit()

#!/usr/bin/python

#from smtplib import SMTP # Standard connection
from smtplib import SMTP_SSL as SMTP #SSL connection
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

sender = 'willythegarbagedisposal@gmail.com'
receivers = ['s1096820@windesheim.nl']

print(sender)

msg = MIMEMultipart()
msg['From'] = 'willythegarbagedisposal@gmail.com'
msg['To'] = 's1096820@windesheim.nl'
msg['Subject'] = 'simple email via python test 1'
message = 'This is the body of the email line 1\nLine 2\nEnd'
msg.attach(MIMEText(message))

ServerConnect = False
try:
    smtp_server = SMTP('smtp.gmail.com','465')
    smtp_server.login('willythegarbagedisposal@gmail.com', 'Willy1234')
    ServerConnect = True
except SMTPHeloError as e:
    print ("Server did not reply")
except SMTPAuthenticationError as e:
    print ("Incorrect username/password combination")
except SMTPException as e:
    print ("Authentication failed")

if ServerConnect == True:
    try:
        smtp_server.sendmail(sender, receivers, msg.as_string())
        print ("Successfully sent email")
    except SMTPException as e:
        print ("Error: unable to send email"), e
    finally:
        smtp_server.close()