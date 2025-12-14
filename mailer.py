from email.message import EmailMessage
import config

def sendMail(formatted_text):
    mail = EmailMessage()
    mail["From"] = config.SENDER_MAIL
    mail["To"] = config.RECEPIENT
    mail["Subject"] = config.SUBJECT
    mail.add_alternative(formatted_text, subtype="html")

    config.SERVER.starttls()
    config.SERVER.login(config.SENDER_MAIL, config.SMTP_PASSWD)

    config.SERVER.sendmail(config.SENDER_MAIL, config.RECEPIENT, mail.as_string())