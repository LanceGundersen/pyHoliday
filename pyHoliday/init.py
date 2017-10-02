#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Initializing file for pyHoliday.

    This file grabs the values from the config.yml file to be used throughout
    the program(s)

    Ideas:
    - Automate the importing. Not sure if it would be effective or not. As this
    is currently specific to what programs require.
"""

import yaml

configFilePath = 'config.yml'

with open(configFilePath, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    continuousRun = cfg['setup']['loop']
    sleep = int(float(cfg['setup']['sleep']))
    platform = cfg['setup']['platform']
    # Audio Files
    intro = cfg['alarm']['intro']
    alarm = cfg['alarm']['alarm']
    voice = cfg['alarm']['voice']
