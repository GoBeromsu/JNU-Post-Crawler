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

def get_credentials():
    try:
        EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
        if EMAIL_ADDRESS and EMAIL_PASSWORD:
            return EMAIL_ADDRESS, EMAIL_PASSWORD
        else:
            # Read from a file or any other methods
            with open("credentials.txt", "r") as f:
                print(f)
                EMAIL_ADDRESS = f.readline().strip()
                EMAIL_PASSWORD = f.readline().strip()
            return EMAIL_ADDRESS, EMAIL_PASSWORD
    except Exception as e:
        print(f"An error occured while reading credentials: {e}")
        return None

def send_email(subject, message):
    try:
        EMAIL_ADDRESS, EMAIL_PASSWORD = get_credentials()
        
        print("【MessageEmail송신시작】：" + str(datetime.now()))
        
        msg = MIMEMultipart()
        msg["Subject"] = "소프트웨어 중심 사업단 공지 등장"
        msg["To"] = EMAIL_ADDRESS
        msg["From"] = EMAIL_ADDRESS
        msg.attach(MIMEText(message))

        # 메일송신처리
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print(message)
        server.quit()

        
        print("Success: Email sent!")
    except Exception as e:
        print("Email failed to send.")
        print(f"An error occured: {e}")

def check_for_new_posts(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        today = datetime.now().date()
        t = soup.findAll('td',attrs={"class":"alignLeft"})
        //추후 수정 
        post_date_tags = soup.select("#content > div.boardContainer > div > table > tbody > tr > td.alignLeft > a > span > em")
        post_title_tags = soup.select("#content > div.boardContainer > div > table > tbody > tr > td.alignLeft > a > strong")
        post_urls = soup.select("#content > div.boardContainer > div > table > tbody > tr > td.alignLeft > a")
        
        for date_tag, title_tag,post_url in zip(post_date_tags, post_title_tags,post_urls):
            post_title = title_tag.text
            url = "https://www.sojoong.kr/www/notice/view/"+  re.compile("[0-9]{3,5}").search(post_url['href']).group() 
            if date_tag.text != today:
                send_email("New post on website", f"Title: {post_title}\nURL: {url}")
                break
            else:
                print("date time is not matched")
    except Exception as e:
        print(f"An error occured: {e}")



check_for_new_posts("https://www.sojoong.kr/www/notice/")

