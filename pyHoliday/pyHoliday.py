#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Entry file for pyHoliday.

    This file displays the current configuration and allows the users to select
    a program from the list.

    Ideas:
    - Look at the programs directory and return the list to be selected.
    - Allow the user to edit the config.yml here.
"""

import pyHoliday.init as i
import pyHoliday.programs.alarm as a
import pyHoliday.init as i


def config():
    print('Continuous Running: ' + str(i.continuousRun))
    print('Time Between Running: ' + str(i.sleep))
    print('Platform: ' + i.platform)
    return


print('\nWelcome to pyHoliday!\n')
config()
print('Continue? Y/n')
c = input()
if(c == 'y' or 'Y' or 'yes' or 'Yes' or 'YES' or ''):
    print('Select Program from list: Enter the number:\n')
    print('1. Light & Audio Trigger')
    p = input()
    if(p == '1'):
        print('Program 1 selected, enjoy!')
        a.alarm()
    else:
        print('No program selected, exiting...')
elif(c == 'n' or 'N' or 'No' or 'NO'):
    print('Exiting..')
