import os
from datetime import datetime, date, timedelta
from pytz import timezone
from github import Github

today = str(datetime.now().date()).replace("-", ".")
yesterday = str(date.today() - timedelta(1)).replace("-", ".")

GITHUB_ACCESS_KEY = os.environ.get("GITHUB_ACCESS_KEY")
g = Github(GITHUB_ACCESS_KEY)
repo_url = "GoBeromsu/JNU-Post-Crawler"

def get_repo(repo_url):
    return g.get_repo(repo_url)

def get_issue(repo_url, issue_num):
    issue = get_repo(repo_url).get_issue(number=issue_num)
    return issue.body

def update_issue(repo_url, issue_num, content):
    issue = get_repo(repo_url).get_issue(number=issue_num)
    issue.edit(body=content)

def create_issue(repo_url, title, content):
    issue = get_repo(repo_url).create_issue(title=title, body=content)

def check_today_issue_created(repo_url):
    repo = get_repo(repo_url)
    now = datetime.now(timezone('Asia/Seoul')) - timedelta(1)
    day_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    issues = repo.get_issues(state='open', since=day_start)
    
    for issue in issues:
        if issue.title == today:
            return True
    return False

# create_issue(repo_url, today, "이렇게 하는거 맞나?")
# print(check_today_issue_created(repo_url))
