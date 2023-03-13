# JNU POST CRAWLER

## 기술 스택

### 프레임워크 및 기술:

- Python 프로그래밍 언어
- requests 라이브러리: HTTP 요청을 보내기 위한 라이브러리
- BeautifulSoup 라이브러리: HTML 및 XML 문서를 파싱하기 위한 라이브러리
- datetime 라이브러리: 날짜 및 시간을 다루기 위한 라이브러리
- smtplib 라이브러리: SMTP 서버와 통신하여 이메일을 보내기 위한 라이브러리
- re 라이브러리: 정규식을 사용하여 문자열을 처리하기 위한 라이브러리

### 기능:

1. get_credentials(): Gmail 계정의 이메일 주소와 비밀번호를 가져오는 함수
2. send_email(subject, message): 이메일 알림을 보내는 함수
3. check_for_new_posts(url): 웹 사이트에서 새 게시물을 확인하는 함수
4. 정규식을 사용하여 게시물의 ID를 게시물 URL에서 추출하는 기능

### 상세한 기능 설명:

1. get_credentials():
    - Gmail 계정의 이메일 주소와 비밀번호를 가져오는 함수
    - 환경 변수에 저장된 자격 증명 또는 credentials.txt 파일에서 자격 증명을 가져옴
    - 반환 값: 이메일 주소와 비밀번호를 담은 튜플
2. send_email(subject, message):
    - 이메일 알림을 보내는 함수
    - smtplib 라이브러리를 사용하여 Gmail 서버에 연결하고, 이메일을 보냄
    - 반환 값: 없음
3. check_for_new_posts(url):
    - 웹 사이트에서 새 게시물을 확인하는 함수
    - requests 라이브러리를 사용하여 GET 요청을 보내고, BeautifulSoup 라이브러리를 사용하여 HTML 응답을 구문 분석함
    - CSS 선택자를 사용하여 게시물의 제목, 게시일 및 URL을 가져옴
    - datetime 라이브러리를 사용하여 오늘 게시된 게시물인지 확인함
    - 오늘이라면 send_email() 함수를 사용하여 이메일 알림을 보내고, 그렇지 않으면 반복함
    - 반환 값: 없음
4. 정규식을 사용하여 게시물의 ID를 게시물 URL에서 추출하는 기능:
    - re 라이브러리를 사용하여 게시물 URL에서 게시물 ID를 추출함
    - 반환 값: 게시물 ID
## 설명
This code is a web crawler that checks for new posts on the website "https://www.sojoong.kr/www/notice/" and sends an email notification if a new post is found. 

The email notification includes the title of the post and the post's URL.

The code is divided into several functions:

get_credentials() is used to get the email address and password for the Gmail account that will be used to send the email notification. The credentials can be stored in environment variables or in a file named credentials.txt in the same directory as the script.
send_email(subject, message) is used to send the email notification. It uses the smtplib library to connect to the Gmail server and send the email.
check_for_new_posts(url) is used to check the website for new posts. It uses the requests library to make a GET request to the website and the BeautifulSoup library to parse the HTML response. It then uses CSS selectors to find the post's title, post's creation date and post's url. It uses datetime library to check if the post is made today, if it is it sends the email notification, if not it continues the loop.
check_for_new_posts("https://www.sojoong.kr/www/notice/") is the function call to start the crawler.
The code also uses the re library to extract the post's id from the post's url.

You can schedule this script to run once an hour using crontab or windows task scheduler.

It's important to note that the credentials for the Gmail account must be kept secure, and not to share the credentials file with anyone.

In order to use the code you will need to install the following python packages: requests, beautifulsoup4, email and re.
You can install them by running:

Copy code
pip install requests beautifulsoup4 email re
Also, if you're using gmail, you need to allow less secure apps to access your account.

This code is just an example, it's recommended to customize it to fit your needs
