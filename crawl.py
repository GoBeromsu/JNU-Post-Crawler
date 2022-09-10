import requests
import re
from bs4 import BeautifulSoup

sw = "https://sw.jnu.ac.kr/"

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
