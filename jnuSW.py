import json
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
# 웹페이지에서 데이터를 가져올 URL
url = 'https://sw.jnu.ac.kr/sw/8250/subview.do'

today = str(datetime.now().date())
today.replace("-",".")

def getTodaySojoong():
    post = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for tr in soup.findAll('tr', attrs={'class':'notice'}):
        tds = tr.findAll('td')
        date = re.search(r'">(.*?)</td>',str(tds[3])).group(1)
        if date == today:
            break
        text = tds[1]
        title = re.search(r'<strong>(.*?)</strong>', str(text)).group(1)
        href = re.search(r'<a\s.*?href=[\'"]?([^\'" >]+)',str(text)).group(1)
        postUrl = "https://sw.jnu.ac.kr/"+href
        post_data = {
            'category':"소프트웨어 공학과",
            'title': title,
            'url': postUrl
        }

        post.append(post_data)
        print(f"Adding... {date} : {title}")   
    return post
