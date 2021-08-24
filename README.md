# Tini

## Description

Simple tool to initialize a software development project

## Motivation
When I begin projects, the setup is mostly the same every time. I open the same applications, run git init then run the commands to initialize the project based on what stack I am using (this is usually the only thing that really changes). So why not have one command that does it all for me.


## Requirements

- Python 3
- Bash

## Setup

- Clone the tini project into desired folder
- Run the following commands
    - python3 -m venv env
    - pip install -r requirements.txt
- Update the file path (line 3) in [tini.sh](http://tini.sh) accordingly
- Add the following command to your bash profile, replacing the file path accordingly
    - source ~/path/to/tini.sh
- Configure DEV_PATH, G_TOKEN, and DEV_APPS environment variables **(optional, will be prompted if not set up)**
    - DEV_PATH = path to where you store your projects (e.g. ~/Documents/Projects)
    - G_TOKEN = github personal access token. Documentation for this can be found here
    - DEV_APPS = an array of any applications you want opened ["Spotify", "Figma", "Notion"]
- Run the command "tini" in the terminal and follow the prompts

## Notes
This application was setup for my current development reality. I develop on MacOS and I work primarily with NodeJS and Python. I use VS code as my editor and  Github for my VCS. I do have intentions on refactoring to make the code more universal but for now, if you intend to use this tool, some tweaks to the code may be necessary for this tool to be effective for you.