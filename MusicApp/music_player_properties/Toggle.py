import pygame


class Pause:
    def __init__(self):
        self._is_paused = False

    def toggle(self):
        if self._is_paused:
            pygame.mixer.music.unpause()
            self._is_paused = False
        else:
            pygame.mixer.music.unpause()
            self._is_paused = True
