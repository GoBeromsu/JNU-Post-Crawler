from github import Github


g = Github("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")
GITHUB_ID = "310o"
repo_url = "GoBeromsu/JNU-Post-Crawler"

def getIssue(issue_num):
    issue = g.get_repo(repo_url).get_issue(number=issue_num)
    return issue.body


def updateIssue(issue_num, content):
    issue = g.get_repo(repo_url).get_issue(number=issue_num)
    issue.edit(body=content)


def createIssue(content, date):
    issue = g.get_repo(repo_url).create_issue(title=date, body=content)
