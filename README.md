# JNU POST CRAWLER
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
