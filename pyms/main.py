import os
import sys
import subprocess

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer
import pygame

# make local imports work
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from frontends.textual.main import MusicPlayer
from control import Control


def Pygame_Init():
    try:
        file = sys.argv[1]
    except IndexError as e:
        print('file not found')
        exit(1)
    finally:
        pass

    pygame.init()
    mixer.music.load(file)
    mixer.music.play()


Pygame_Init()


# textual init
App = MusicPlayer()
App.run()
exit()
