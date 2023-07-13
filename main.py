import os
import requests
import bs4
import smtplib
from datetime import datetime
import time
import re
import yaml
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from jnuSW import *
from sojoong import *
from issue import *
from dotenv import load_dotenv



class EmailSender:
    def __init__(self, to_addresses):
        self.to_addresses = to_addresses
        load_dotenv()
        self.email_address = os.getenv('EMAIL_ADDRESS')
        self.email_password = os.getenv('EMAIL_PASSWORD')
        self.server = smtplib.SMTP("smtp.gmail.com", 587)

        print("email/password : ",self.email_address, self.email_password)
    def login(self):
        self.server.starttls()

        self.server.login(self.email_address, self.email_password)

    def send_email(self, message, subtitle, category):
        try:
            print(f"{datetime.now()} Email sending... ")
            msg = MIMEMultipart()
            msg["Subject"] = f"[{category}] " + subtitle
            msg["To"] = ', '.join(self.to_addresses)
            msg["From"] = self.email_address
            msg.attach(MIMEText(message))

            self.server.send_message(msg)
            print("Success: Email sent!")
        except Exception as e:
            print("Email failed to send.")
            print(f"An error occured: {e}")

    def close(self):
        self.server.quit()


def process_posts():
    with open('user.yml') as file:
        user_data = yaml.full_load(file)
    to_addresses = user_data['users']

    posts = [get_today_jnuSW(), get_today_sojoong()]
    email_sender = EmailSender(to_addresses)
    email_sender.login()

    for post in posts:
        if post is None:
            continue
        for p in post:
            category, subtitle, message = p["category"], p["title"], p["url"]
            try:
                email_sender.send_email(message, subtitle, category)
            except Exception as e:
                print(f"An error occured while sending email: {e}")
                email_sender.send_email(f"An error occured while sending email: {e}", "Error Occured in sending Message", category)
    email_sender.close()

if __name__ == "__main__":
    process_posts()
