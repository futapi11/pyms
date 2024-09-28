import os
import sys
import pygame
from pygame import mixer

class Control:

    def play_pause():
        if mixer.music.get_busy() is True:
            mixer.music.pause()
        else:
            mixer.music.unpause()

    def quit():
        mixer.music.stop()
        sys.exit(0)

    def fast_forward():
        current_time = mixer.music.get_pos() / 750
        new_time = current_time + 15
        pygame.mixer.music.set_pos(new_time)

    def rewind():
        current_time = mixer.music.get_pos() / 750
        new_time = current_time - 15
        if new_time < 0:
            pygame.mixer.music.set_pos(0)
        else:
            pygame.mixer.music.set_pos(new_time)
