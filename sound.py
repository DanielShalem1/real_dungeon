import sys

print(sys.path)

import pygame

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()