import csv
import smtplib
from email.message import EmailMessage

def read_contacts(filename):

    with open(filename, mode= "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
    return rows

def send_email(sender, password, recipient_name, recipient_email):
    msg = EmailMessage()
    msg["from"] = sender
    msg["to"] = recipient_email
    msg["subject"] = "Hello!"
    msg.set_content(f'''
    Hi! {recipient_name},
    I hope you're having a good day!!
    See yaaa!
    ''')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


if __name__ == "__main__":
    sender = "YOUR_EMAIL@gmail.com"
    password = "YOUR_APP_PASSWORD"
    contacts = read_contacts("email.csv")
    for contact in contacts:
        send_email(sender, password, contact["name"], contact["email"])
