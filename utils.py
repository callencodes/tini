import sys
import os
import json

from github import Github
from dotenv import load_dotenv

load_dotenv()
DEV_PATH = os.getenv("DEV_PATH")

def initialize(propname, propval, name):
  FOLDER_PATH = f"{DEV_PATH}/{name}"

  def createFolder(message):
    try:
      os.chdir(DEV_PATH)
      os.mkdir(name)
      return json.dumps({ 'message': f'Created folder {name}'})
    except FileExistsError:
      return json.dumps({ 'message': f'Folder {name} already exists, {message}'})

  def initializeRepository(vcs):
    if not vcs:
      return
    user = Github(os.getenv("G_TOKEN")).get_user()
    import pdb;pdb.set_trace()
    repo = user.create_repo(name)
    os.chdir(FOLDER_PATH)
    os.system(f"echo \"# {name}\nA new application.\" >> README.md")
    os.system("git init")
    os.system("git add README.md")
    os.system("git commit -m \"first commit\"")
    os.system("git branch -M main")
    os.system(f"git remote add origin https://github.com/{repo.full_name}")
    os.system("git push -u origin main")
    return json.dumps({ 'message': f'Initialized {name} on Github'})

  def initializeStack(stack):
    if stack == 'MERN':
      try:
        os.chdir(FOLDER_PATH)
      except:
        createFolder("MERN")
        os.chdir(FOLDER_PATH)
      
      os.mkdir("server")
      os.chdir(FOLDER_PATH)
      os.system("npm install -g express")
      os.system("npm install")
      os.system("npm install mongoose")
      os.chdir(FOLDER_PATH)
      os.system("npx create-react-app client")
      os.system("npm install concurrently --save-dev")
      os.system("npm install nodemon --save-dev")
      
    if stack == 'Python-Django':
      os.system("python3 -m venv env")
      os.system(". env/bin/activate")
      os.system("pip install Django")
      os.system(f"django-admin startproject {name}")

    return json.dumps({ 'message': f'Installed neccessary dependencies for a {stack} application'})

  def initializeAPIArch(api):
    try:
      os.chdir(FOLDER_PATH)
    except:
      createFolder("API")
      os.chdir(FOLDER_PATH)
      
    if api == 'Node':
      os.system("npm init")
      os.system("npm install --save express mongodb body-parser")
      os.system("npm install --save-dev nodemon")
    else:
      os.system("python3 -m venv env")
      os.system(". env/bin/activate")
      os.system("python3 -m pip install flask_restful")
      os.system("python3 -m pip install flask_sqlalchemy")

    return json.dumps({ 'message': f'Installed neccessary dependencies for a {api} api'})

  funcs = {
    'stack': initializeStack,
    'api': initializeAPIArch,
    'vcs': initializeRepository,
    "_default": 'Nothing to do'
  }

  func = funcs[propname] if propname in funcs else funcs["_default"]
  result = func(propval)
  
  if result:
    return result