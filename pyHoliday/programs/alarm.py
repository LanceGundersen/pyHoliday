#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Halloween Alarm and Light Program aka alarm.

    This file controls all aspects of the alarm program. It has the unique
    scripts to run on linux and chip at the moment. Linux doesn't have the
    light/relay trigger based on hardware limitations as I know it.

    Ideas:
    - Look into if the nested if/while statements are the best way to run this
    program
    - Add Pi Support
    - For Linux/PC add Arduino support for relays
    - For Linux/PC add wireless WiFi Relay Support
"""

import pyHoliday.functions as f
import pyHoliday.init as i
import time


def linux():
    print(alarm)
    f.playAudio(i.alarm)
    f.playAudio(i.voice)
    return


def chip():
    import CHIP_IO.GPIO as GPIO
    trigger = i.cfg['chip']['trigger_pin']
    light = i.cfg['chip']['relay_pin']
    GPIO.setup(trigger, GPIO.OUT)
    GPIO.setup(light, GPIO.OUT)
    GPIO.output(light, GPIO.HIGH)
    f.playAudio(i.intro)
    f.playAudio(i.alarm)
    f.playAudio(i.voice)
    GPIO.output(light, GPIO.LOW)
    return


def alarm():
    f.playAudio(i.intro)
    if(i.platform == 'Linux' or 'linux'):
        if(i.continuousRun):
            while(i.continuousRun):
                linux()
                time.sleep(i.sleep)
        else:
            linux()
        return
    elif(i.platform == 'Chip' or 'chip'):
        if(i.continuousRun):
            while(i.continuousRun):
                chip()
                time.sleep(i.sleep)
        else:
            chip()
