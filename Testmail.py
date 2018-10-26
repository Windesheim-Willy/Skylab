import smtplib

sender = 'marc@vanwaltmeijer.nl'
receivers = ['familie@vanwaltmeijer.nl']

message = """From: From MarcvWM <marc@vanwaltmeijer.nl>
To: To Famvwm <familie@vanwaltmeijer.nl>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.vanwaltmeijer.nl')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
