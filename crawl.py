import requests
import re
from bs4 import BeautifulSoup

url = "https://sw.jnu.ac.kr/sw/8250/subview.do;jsessionid=7CA6DD21555BC61E000DF99019AD2C03?enc=Zm5jdDF8QEB8JTJGYmJzJTJGc3clMkYxMDM4JTJGYXJ0Y2xMaXN0LmRvJTNG"
sw ='https://sw.jnu.ac.kr/'

def getHtml(url):
    html = requests.get(url)
    return BeautifulSoup(html.text, "html.parser")

def getSWPost(html):    
    for a in getHtml(url).find_all("tr", "notice"):
        subject = a.find("td", "td-subject")
        print(re.sub(r"\n", "", subject.text))  # 공지 제목
        print(sw+subject.find("a")["href"])# 공지 링크, 뒤에 인덱싱만 저장해뒀군
        print(a.find("td", "td-date").text)  # 날짜
        print("------------------------------")
# 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
print(getSWPost(getHtml(url)))