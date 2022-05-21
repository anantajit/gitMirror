from github import Github

access_token_api_file = open("access_token.api")

access_token = access_token_api_file.readline().strip()

g = Github(access_token)

for repo in g.get_user().get_repos():
    print(repo.name)
