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
from issue import *


def sendEmail(message, subtitle, category):
    try:

        EMAIL_ADDRESS, EMAIL_PASSWORD = "gobeumsu@Gmail.com", "vtbkxdgvyoxveloe"
        print(f"{datetime.now()} Email sending... ")
        msg = MIMEMultipart()
        msg["Subject"] = f"[{category}] " + subtitle
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
    # TODO: issue가 있다면 issue를 가져온다
    # TODO: issue가 없다면, 바로 실행을 하고, issue에 오늘의 데이터를 json 형식으로 입력 한다.
    for post in posts:
        if post == None:
            continue
        for p in post:
            category, subTitle, message = p["category"], p["title"], p["url"]
            try:
                # print(p)
                sendEmail(message, subTitle, category)
            except Exception as e:
                print(f"An error occured while sending email: {e}")
                sendEmail(f"An error occured while sending email: {e}", "Error Occured in sending Message", category)


start()
