import configparser
import smtplib

config = configparser.ConfigParser()
config.read('willy.ini')

sender = config['DEFAULT']['GMAIL'] # Willy Gmail account
sender_ww = config['DEFAULT']['GMAIL-WW'] # Willy Gmail wachtwoord

lijst = ['dylan.reimerink@windesheim.nl', 'fabian.vande.bor@windesheim.nl', 'george.wassink@windesheim.nl', 'johnny.borg@windesheim.nl', 'michel.stompe@windesheim.nl', 'sven.pook@windesheim.nl', 'jan-gerrit.elzinga@windesheim.nl', 'johan.int.hout@windesheim.nl', 'marc.van.walt-meijer@windesheim.nl', 'ruben.stuut@windesheim.nl']

# Config in gmail acoount Inloggen en beveiliging / Apps met toegang tot je account / Apps met lagere beveiliging toestaan: AAN

for i in range(len(lijst)):
    gserver = smtplib.SMTP('smtp.gmail.com', 587)
    gserver.ehlo()
    gserver.starttls()
    gserver.login(sender, sender_ww)
    gserver.sendmail(sender, lijst[i], 'Subject:Testmail van Willy\nSpammen vanuit Python werkt!\n\nGroet,\nMarc.')
    gserver.quit()
    print('Bericht verzonden aan ', lijst[i])
