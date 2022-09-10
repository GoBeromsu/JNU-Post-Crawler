import issue
import crawl
from datetime import datetime

url = "https://sw.jnu.ac.kr/sw/8250/subview.do;jsessionid=7CA6DD21555BC61E000DF99019AD2C03?enc=Zm5jdDF8QEB8JTJGYmJzJTJGc3clMkYxMDM4JTJGYXJ0Y2xMaXN0LmRvJTNG"
content=""

def main():    
    content = crawl.getSWPost(crawl.getHtml(url),getToday())
    if (content!=""):   
        issue.createIssue(content, getToday())
    else:
        print("No Content")
        

def getToday():
    return datetime.today().strftime("%Y.%m.%d")

if __name__ == "__main__":
    main()
