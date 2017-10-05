#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Functions file for pyHoliday.

    This file contains universal functions that can/could or should be expected
    to be used throughout the program(s)

    Ideas:
    - Audio playback solution currently requires pygame which seems a bit heavy
    for this use case. Unsure of lighter/simpilier options.
"""

import pygame


# Pass mp3 file in as stream
def playAudio(stream):
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load('pyHoliday/audio/' + stream)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(1000)
    return
