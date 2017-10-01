import pygame


def playAudio(stream):
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load('audio/' + stream)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(1000)
    return
