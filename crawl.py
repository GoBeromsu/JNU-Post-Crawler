import requests
import re
from bs4 import BeautifulSoup

sw = "https://sw.jnu.ac.kr/"
sojoong = "https://www.sojoong.kr/www/notice/"

def getHtml(url):
    html = requests.get(url)
    return BeautifulSoup(html.text, "html.parser")

# 소프트웨어공학과 공지
def getSWPost(html,today):
    text =""
    for a in html.find_all("tr", "notice"):
        date = a.find("td","td-date").text
        if(today==date):
            subject = a.find("td", "td-subject")
            title=re.sub(r"\n", "", subject.text)  # 공지 제목
            link=sw + subject.find("a")["href"]  # 공지 링크
            text+=f"SW {title} {link}\n"
    return text

def getSojoongPost(html,today): 
    text=""
    for a in html.find_all("td","alignLeft"):
        date = a.find("em").text
        if(today==date):
            title = a.find("strong","cutText").text
            link =sojoong+"view/"+  re.compile("[0-9]{3,5}").search(a.find("a")["href"]).group()
            text+=f"SJ {title} {link}\n"
    return text
