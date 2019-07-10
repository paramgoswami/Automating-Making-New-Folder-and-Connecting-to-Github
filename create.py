from github import Github
import sys
import os

path = "\\Users\\param\\Desktop\\Projects" #The Path of Folder in which you want to create your Folder of Project

username=""#your Github Username
password="" #Your Github Password

if len(sys.argv) > 1:#only execute if a project name is received
    project_name = str(sys.argv[1])
    os.makedirs(path + "\\"+ project_name) #making new folder named project name
    g=Github(username,password)
    user=g.get_user()
    repo=user.create_repo(project_name) #Creating a github repository named project name
    print("The repo has been created successfully")
    