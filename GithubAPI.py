import unittest
import requests
import json


 
def git_data(userid):
    """Given the Github userid and return name of repo and number of commits"""
    commit_count = 0
    dict = {}
    get_repository = requests.get(f"https://api.github.com/users/{userid}/repos")
    repository_data =get_repository.json()
    for entry in repository_data:
        name = entry['name']

        get_commits = requests.get(f"https://api.github.com/repos/{userid}/{name}/commits")
        commit_data = get_commits.json()
        for entry in commit_data:
            if entry["commit"]:
                commit_count +=1
        dict[name] = commit_count
    return dict
