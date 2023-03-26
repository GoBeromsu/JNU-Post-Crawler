from github import Github
from datetime import datetime,date,timedelta
from pytz import timezone

today = str(datetime.now().date()).replace("-",".")
yesterday = str(date.today() - timedelta(1)).replace("-",".")


g = Github(GITHUB_ACCESS_KEY)
repo_name= "GoBeromsu/JNU-Post-Crawler"
repo = g.get_repo(repo_name)

def getIssue(repo_url,issue_num):
    issue = g.get_repo(repo_url).get_issue(number=issue_num)
    return issue.body

def updateIssue(repo_url,issue_num,content):
    issue = g.get_repo(repo_url).get_issue(number=issue_num)
    issue.edit(body=content)

def createIssue(repo_url,content):
    issue = g.get_repo(repo_url).create_issue(title=today,body=content)

def checkTodayIssueCreated():
    now = datetime.now(timezone('Asia/Seoul')) - timedelta(1)
    day_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    issues = repo.get_issues(state='open', since= day_start)
    for issue in issues:
        if issue.title != today:
            return False
        else:
            return True
