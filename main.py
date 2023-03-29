import os
import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import time
import re
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from jnuSW import * 
from sojoong import *


def sendEmail(message,subTitle ,category):
    try:
        EMAIL_ADDRESS, EMAIL_PASSWORD =os.environ.get('EMAIL_ADDRESS'),os.environ.get('EMAIL_PASSWORD')
        print(f"{datetime.now()} Email sending... " )
        msg = MIMEMultipart()
        msg["Subject"] = f"[{category}] " + subTitle 
        msg["To"] = EMAIL_ADDRESS
        msg["From"] = EMAIL_ADDRESS
        msg.attach(MIMEText(message))

        # 메일송신처리
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print("Success: Email sent!")
    except Exception as e:
        print("Email failed to send.")
        print(f"An error occured: {e}")

def start():
    posts = [getTodayJnuSW(), getTodaySojoong()]
    for post in posts:
        if post ==None:
            continue
        for p in post:
            category,subTitle,message =p["category"],p["title"],p["url"]
            try:
                # print(p)
                sendEmail(message,subTitle,category)
            except Exception as e:
                print(f"An error occured while sending email: {e}")
                sendEmail(f"An error occured while sending email: {e}","Error Occured in sending Message",category)

start()
