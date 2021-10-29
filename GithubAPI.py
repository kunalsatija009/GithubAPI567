import requests
import json

def commit_count(userID):
    """This Function will count the number of commits"""
    repos =  get_repository(userID)
    dict = {}
    for entry in repos:
        name = entry['name']
        dict[name] = get_commits(userID, name)
    return dict
        
def  get_repository(userID):
    """This function will get the repository of the userid entered"""
    getRepo = requests.get(f"https://api.github.com/users/{userID}/repos").json()
    return getRepo

def get_commits(userID, name):
    """This function will get the commits of the userid entered"""
    commitURL = requests.get(f"https://api.github.com/repos/{userID}/{name}/commits").json()
    return len(commitURL)