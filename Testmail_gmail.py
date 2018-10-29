#start diverse modules
from start_willy import *

# Aanpassen in google account voor gmail => Config in gmail acoount Inloggen en beveiliging / Apps met toegang tot je account / Apps met lagere beveiliging toestaan: AAN


# Ophalen emailaders en wachtwoord van account uit willy.ini uit dezelfde directory

config = configparser.ConfigParser()
config.read('willy.ini')

sender = config['DEFAULT']['GMAIL'] # Willy Gmail account
sender_ww = config['DEFAULT']['GMAIL-WW'] # Willy Gmail wachtwoord

#Lijst met emailadressen waarnaartoe moet worden gestuurd
aantal_email 


for i in range(len(lijst)):

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = sender

    # storing the receivers email address
    msg['To'] = lijst[i]

    # storing the subject
    msg['Subject'] = "Alweer een testmail met attachment"

    # string to store the body of the mail
    body = "Dit moet een mail met een attachment zijn.\n\nGroet,\nMarc."

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "willy.png"
    attachment = open(filename, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    gserver = smtplib.SMTP('smtp.gmail.com', 587)
    gserver.ehlo()
    gserver.starttls()
    gserver.login(sender, sender_ww)

    text = msg.as_string()

    gserver.sendmail(sender, lijst[i], text)
    gserver.quit()
    print('Bericht verzonden aan ', lijst[i])
