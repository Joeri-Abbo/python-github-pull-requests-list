import os

import yaml
from github import Github

config = yaml.safe_load(open(os.path.dirname(__file__) + '/config.yml'))

if __name__ == '__main__':
    g = Github(login_or_token=config['token'], per_page=1000)
    for repo in g.get_user().get_repos():
        count = repo.get_pulls("open").totalCount
        if not count == 0:
            print(repo.html_url)
            print(count)
