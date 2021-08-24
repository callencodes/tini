import os
import re
import json
import pdb
import webbrowser
from datetime import datetime
import utils

import click
import six
from PyInquirer import (Token, ValidationError, Validator, prompt, style_from_dict)
from pyfiglet import figlet_format
from dotenv import load_dotenv

load_dotenv()

try:
  import colorama
  colorama.init()
except ImportError:
  colorama = None

try:
  from termcolor import colored
except ImportError:
  colored = None

style = style_from_dict({
  Token.QuestionMark: '#fac731 bold',
  Token.Answer: '#4688f1 bold',
  Token.Instruction: '',  # default
  Token.Separator: '#cc5454',
  Token.Selected: '#0abf5b',  # default
  Token.Pointer: '#673ab7 bold',
  Token.Question: ''
})

def welcome(string, color, font="slant", figlet=False):
  if colored:
    if not figlet:
      six.print_(colored(string, color))
    else:
      six.print_(colored(figlet_format(string, font=font), color))
  else:
    six.print_(string)

def openWindows(DEV_APPS):
  for app in DEV_APPS:
      os.system(f"open /Applications/{app}.app")
  return json.dumps({ 'message': f'opened {DEV_APPS}'})

def configInfo():
  initial = [
    {
      'type': 'input',
      'name': 'dev_path',
      'message': 'Full path to dev directory: '
    },
    {
      'type': 'input',
      'name': 'github_token',
      'message': 'Github token: '
    },
    {
      'type': 'input',
      'name': 'dev_apps',
      'message': 'Apps to open (seperated by commas, ex. Spotify, Figma): '
    }
  ]
  answers = prompt(initial, style=style)
  os.environ['DEV_PATH'] = answers['dev_path']
  os.environ['G_TOKEN'] = answers['github_token']
  os.environ['DEV_APPS'] = answers['dev_apps']
  print("Information initalized. You can now use Tini.")

def askProjectInfo():
  initial = [
    {
      'type': 'input',
      'name': 'name',
      'message': 'Project Name:'
    },
    {
      'type': 'list',
      'name': 'type',
      'message': 'What type of project is this?',
      'choices': ['Full Stack', 'API']
    }
  ]
  answers = prompt(initial, style=style)
  
  if answers['type'] == 'Full Stack':
    web_stack = [
    {
      'type': 'list',
      'name': 'stack',
      'message': 'What stack will this project utilize?',
      'choices': ['MERN (MongoDB, Express, React, Node)',
                  'Python-Django'
                ],
      'filter': lambda v: v.split(' (')[0]
    },
    ]
    ws_answers = prompt(web_stack, style=style)
    answers.update(ws_answers)
  
  if answers['type'] == 'API':
    api_arch = [
      {
        'type': 'list',
        'name': 'api',
        'message': 'What language will this API utilize?',
        'choices': ['Node', 'Python-Flask']
      },
    ]
    aa_answers = prompt(api_arch, style=style)
    answers.update(aa_answers)
    
  final_questions =[
    {
      'type': 'confirm',
      'name': 'vcs',
      'message': 'Initialize git repository?',
      'default': True
    },
    {
      'type': 'confirm',
      'name': 'open_windows',
      'message': 'Open all needed applications and windows?',
      'default': False
    }
  ]
  final_answers = prompt(final_questions, style=style)
  answers.update(final_answers)

  return answers

@click.command()
def main():
  """
  Simple CLI to initialize a software development project
  """
  welcome("Tini CLI", color="red", figlet=True)
  welcome("Welcome to Tini CLI", "green")
  if not os.getenv("DEV_PATH") or not os.getenv("G_TOKEN"):
    print("Initial information needed. Please refer to docs here if you need any help.")
    configInfo()
  
  DEV_APPS = os.getenv("DEV_APPS").split(',')
  DEV_PATH = os.getenv("DEV_PATH")

  projectInfo = askProjectInfo()
  for k,v in projectInfo.items():
    if k not in ('name', 'type', 'open_windows'):
      res = utils.initialize(k, v, projectInfo['name'])
      print(res)
  
  os.chdir(f"{DEV_PATH}/{projectInfo['name']}")
  if projectInfo['open_windows']:
    os.system(f"code .")
    openWindows(DEV_APPS)



if __name__ == '__main__':
  main()