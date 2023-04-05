import os
import sys

from pygame import mixer

from music_player_properties.Song import Song

mixer.init()


def play_song(song):
    mixer.music.load(song.get_song_path())
    mixer.music.play()


def pause_song(song):
    mixer.music.pause()


def resume_song(song):
    mixer.music.unpause()


def stop_song():
    mixer.music.stop()

def foward_song(song, offset_val):
    print(song.get_song_path)
    stop_song()
    mixer.music.load(song.get_song_path)
    mixer.music.play(loops=0, start=offset_val)

def is_song_playing():
    return mixer.get_busy()