import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
url = 'https://www.sojoong.kr/www/notice/'
today = str(datetime.now().date()).replace("-",".")

def getTodayJnuSW():
    post = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    t = soup.findAll('td',attrs={"class":"alignLeft"})

    for tr in soup.findAll('td',attrs={"class":"alignLeft"}):
        date = tr.find('em').text
        title = tr.find('strong').text
        href = re.search(r'<a\s.*?href=[\'"]?([^\'" >]+)',str(tr)).group(1)
        postNumber= re.compile("[0-9]{3,5}").search(href).group()
        postUrl = "https://www.sojoong.kr/www/notice/view/"+postNumber
        if date!=today:
            continue
        post.append([title,postUrl])
        print(f"Adding... {date} : {title}")
        return post


