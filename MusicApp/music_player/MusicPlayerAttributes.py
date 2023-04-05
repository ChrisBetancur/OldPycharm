import random
import numpy

import pygame

from music_player.MusicPlayer import MusicPlayer
from music_player_properties.Model import Model
from music_player_properties.Song import Song
from music_player_properties.SongPlayer import play_song, pause_song, resume_song, stop_song, is_song_playing

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)


def shuffle(playlist):
    if playlist is None:
        return
    shuffle_playlist(playlist)
    '''for song in playlist.get_shuffled_playlist():
        print(song.get_song_name())'''
    return playlist_to_player(playlist, True)


def playlist_to_player(playlist, is_shuffled):
    if playlist is None:
        return

    '''for song in playlist.get_shuffled_playlist():
        print(song.get_song_name())'''

    music_player = MusicPlayer()

    music_player.set_model_head(None)

    if is_shuffled is True:
        return shuffled_playlist_to_player(music_player, playlist)

    if is_shuffled is False:
        return default_playlist_to_player(music_player, playlist)


def shuffled_playlist_to_player(music_player, playlist):
    for current_song in playlist.get_shuffled_playlist():
        song = current_song
        model = Model(song)
        append_to_player(music_player, model)

    return music_player


def default_playlist_to_player(music_player, playlist):
    real_music_player = music_player
    for current_song in playlist.get_playlist():
        song = current_song
        model = Model(song)
        append_to_player(real_music_player, model)
    return real_music_player


def append_to_player(music_player, model):
    if music_player.get_model_head() is None:
        music_player.set_model_head(model)
        return
    # print(music_player.get_model_head().get_song().get_song_name())

    current_model = music_player.get_model_head()

    prev_model = None

    while current_model.get_next_model() is not None:
        if current_model.get_next_model().get_next_model() is None:
            prev_model = current_model
        current_model = current_model.get_next_model()

    current_model.set_prev_model(prev_model)
    current_model.set_next_model(model)
    # current_model.get_next_model().set_next_model(music_player.get_model_head())
    music_player.get_model_head().set_prev_model(model)
    # print(music_player.get_model_head().get_next_model().get_song().get_song_name())


def make_player_circular(music_player):

    if music_player is None:
        return
    current_model = music_player.get_model_head()

    prev_model = None
    while current_model.get_next_model() is not None:
        if current_model.get_next_model().get_next_model() is None:
            prev_model = current_model
        current_model = current_model.get_next_model()

    current_model.set_next_model(music_player.get_model_head())
    current_model.set_prev_model(prev_model)


def shuffle_playlist(playlist):
    shuffled_playlist = playlist.get_song_list().copy()

    '''for song in shuffled_playlist:
        print(song.get_song_name())'''

    for index in range(0, len(shuffled_playlist) - 1):
        random_index = random.randint(0, len(shuffled_playlist) - 1)
        if random_index == index:
            random_index = random.randint(0, len(shuffled_playlist) - 1)

        temp = shuffled_playlist[index]
        shuffled_playlist[index] = shuffled_playlist[random_index]
        shuffled_playlist[random_index] = temp

    playlist.set_shuffled_playlist(shuffled_playlist)

    '''for song in shuffled_playlist:
        print(song.get_song_name())'''


def start_music_player_demo(music_player):
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    screen.fill((255, 255, 255))
    make_player_circular(music_player)
    current_model = music_player.get_model_head()
    # current_model.get_prev_model().get_next_model().set_next_model(music_player.get_model_head())

    running = True
    play_song(current_model.get_song())

    print(current_model.get_song().get_song_name(), "is now playing...")
    is_song_playing()
    is_pause_song = False

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == SONG_END:
                current_model = current_model.get_next_model()
                play_song(current_model.get_song())
                print(current_model.get_song().get_song_name(), "is now playing...")

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if is_pause_song is False:
                        print("Entered")
                        pause_song(current_model.get_song())
                        is_pause_song = True
                    elif is_pause_song is True:
                        resume_song(current_model.get_song())
                        is_pause_song = False

                elif event.key == pygame.K_LEFT:
                    current_model = current_model.get_prev_model()
                    play_song(current_model.get_song())
                    print(current_model.get_song().get_song_name(), "is now playing...")
                elif event.key == pygame.K_RIGHT:
                    current_model = current_model.get_next_model()
                    play_song(current_model.get_song())
                    print(current_model.get_song().get_song_name(), "is now playing...")


def print_player(music_player):
    model_head = music_player.get_model_head()

    if model_head is not None:
        current_model = model_head
        while current_model is not None:
            print(current_model.get_song().get_song_name())
            current_model = current_model.get_next_model()
