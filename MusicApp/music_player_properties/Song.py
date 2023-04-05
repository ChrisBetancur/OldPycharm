import pygame
from mutagen.mp3 import MP3

class Song:
    def __init__(self, song_name):
        self._song_name = song_name

    def __init__(self, song_path, song_name, song_author):
        self._song_path = song_path
        self._song_name = song_name
        self._song_author = song_author
        pygame.mixer.music.load(self._song_path)
        song_length = MP3(song_path)
        self._song_length = song_length.info.length

    def get_song_path(self):
        return self._song_path

    def set_song_path(self, song_path):
        self._song_path = song_path

    def get_song_name(self):
        return self._song_name

    def set_song_name(self, song_name):
        _song_name = song_name

    def get_song_author(self):
        return self._song_author

    def set_song_author(self, song_author):
        self._song_author = song_author

    def get_song_length(self):
        return self._song_length

    def set_song_length(self, song_length):
        self._song_length = song_length
