import subprocess
import os
from github import Github

# supplied by config file

args = ""

working_directory = "../test/repos"

########

access_token_api_file = open("access_token.api")

access_token = access_token_api_file.readline().strip()


print("Attempting to access GitHub using provided access token...")
g = Github(access_token)

repo_object = g.get_user().get_repos()

print("Getting existing repositories on GitHub...")

repo_list = []

for repo in repo_object:
    repo_list.append(repo.name)

# repo list contains the list of github repositories that already exist
print("Mirroring private repositories...")
repo_list_file = open("repos.config")

for repository in repo_list_file:
    # check if we need to create a new repository or not 
    # ignore commented out lines
    if(repository[0] == "#"):
        print(repository)
        continue

    repo_data = repository.strip().split(",")

    repo_name = repo_data[0].strip()
    repo_url = repo_data[1].strip()

    if(not (repo_name in repo_list)):
        print("Creating a new repo on GitHub for " + repo_name)
        repo = g.get_user().create_repo(repo_name,private=True) # by default, mirrored repositories 
        # are kept private until mirroring works as intended. The switch to public is not to be 
        # controlled by this utility

    # we have a guaranteed corresponding github repository now
    print("Pulling private repository...")
    
    repo_path = working_directory + "/" + repo_name

    if(not os.path.isdir(repo_path)):
        print("Cloning repository...")
        subprocess.call('./clone_private_repo.sh ' + repo_url + " " + working_directory + "/" + repo_name + " " + "git@github.com:" + g.get_user().login + "/" + repo_name, shell=True)

    print("Pulling latest changes...")
    subprocess.call('./pull_private_repo.sh ' + working_directory + "/" + repo_name, shell=True)
    
    # now, we push the repo to github
    print("Pushing to GitHub...")
    
    subprocess.call('./push_github_repo.sh ' + working_directory + "/" + repo_name, shell=True)
    print("Mirror complete for " + repo_name)
