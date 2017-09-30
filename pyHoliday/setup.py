import os
import yaml
import requests

configFile = os.path.exists('config.yml')
configFileUrl = 'http://github.com/'
download = requests.get(configFileUrl)

if (configFile):
    print('Configuration exists! Do you wish to edit? Enter n/Y')
else:
    print('Configuration file missing! Downloading...')


def editConfig():
    with open(configFile, 'r') as f:
        data = yaml.load(f)
    print(data)
    return


def getConfig():
    open('config.yml', 'wb').write(download.content)
    return

# Check Desired platform
# print('What platform do you wish to run?')
# print('Enter 1 for chip, 2 for PC')
# platform = input()
# if (platform == '1'):
#     print('Chip Selected')
# elif (platform == '2'):
#     print('PC Selected')
#     config = open("config.txt", "w")
#     config.write("platform:pc")
#     config.close()
# return
