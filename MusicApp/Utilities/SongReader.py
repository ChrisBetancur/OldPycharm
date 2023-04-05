import os

from music_player_properties.Playlist import Playlist
from music_player_properties.Song import Song


def get_song_path(file):
    dir_path = os.path.realpath(file)
    #print(os.path.realpath(file))
    dir_path = "C:/Users/chris/PycharmProjects/MusicPlayerApplication/" + file
    # print(os.path.dirname("C:/Users/chris/PycharmProjects/MusicPlayerApplication/SongList"))
    song_paths = []

    for root, dirs, files in os.walk(dir_path):
        for current_file in files:
            if current_file.endswith(".mp3"):
                song_paths.append(dir_path + "/" + current_file)
    return song_paths


def get_playlist(song_paths, playlist_name):
    playlist = Playlist(playlist_name)
    song_list = []
    if song_paths is not None:
        for song_path in song_paths:
            actual_song = song_path.split("/")
            song_attributes = actual_song[6].split(" - ")
            song_name = song_attributes[1].split(".mp3")
            song = Song(song_path, song_name[0], song_attributes[0])
            song_list.append(song)
    playlist.set_song_list(song_list)
    return playlist