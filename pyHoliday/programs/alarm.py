import os  # Import os for playing audio streams
import time  # Import time for time baed events
import subprocess

# Continuous Program Run
infiniteRun = True
initStartup = True
platform = 'none'
host = os.uname()
print(initStartup)
print(host)


light = 'CSID0'  # GPIO Light Pin
trigger = 'CSID2'  # GPIO trigger Pin


def setup():
    # Check Desired platform
    print('What platform do you wish to run?')
    print('Enter 1 for chip, 2 for PC')
    platform = input()

    if (platform == '1'):
        print('Chip Selected')
    elif (platform == '2'):
        print('PC Selected')
        config = open("config.txt", "w")
        config.write("platform:pc")
        config.close()
    return


def playAudio(stream):
    p = subprocess.Popen(['mpg321', stream])
    p.wait()
    return


def mainLoop():
    print('In Loop')
    return


while infiniteRun:
    if (initStartup):
        initStartup = False
        print(initStartup)
        setup()
        time.sleep(0.2)
    mainLoop()
    time.sleep(0.2)
