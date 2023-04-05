import os

import pygame
import pygame_gui
from pygame import mixer, time
from pygame.color import Color
from pygame.time import set_timer

from Engine.GUI import Button, button_was_pressed, TimeSlider, ToggleButton, play_command, pause_command, move, \
    shift_by_song, Text, PlaylistDisplay
from ImageReader import Image
from Utilities.Converter import seconds_to_min, get_song_length_str
from Utilities.SongReader import get_song_path, get_playlist

from music_player.MusicPlayerAttributes import SONG_END, make_player_circular, shuffle, print_player
from music_player_properties.SongPlayer import play_song, pause_song, resume_song, is_song_playing

(WIDTH, HEIGHT) = (1500, 1000)
(r, g, b) = (0, 0, 0)
DEFAULT_FONT = "Light 300"
DEFAULT_COLOR = (192, 192, 192)
current_playlist = None

background = Image("C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/background.jpg", [-85, 0])
logo = Image("C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/music_note.png", [460, 150])

# background_image = pygame.image.load("C:/Users/chris/PycharmProjects/MusicPlayerApplication/background.jpg")

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((r, g, b))
pygame.display.flip()


def draw_window(current_model, is_paused):
    screen.fill((r, g, b))
    screen.blit(background.image, background.rect)
    screen.blit(logo.image, logo.rect)

    set_current_song_name_text(current_model.get_song(), is_paused)
    set_buttons(is_paused)
    set_time_slider(current_model.get_song())

    current_time_txt.draw(screen)
    end_time_txt.draw(screen)

    set_playlist_display()

    pygame.display.update()


time_slider = TimeSlider(730, 660)

play_btn = ToggleButton(command=play_command,
                        image_path="C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/play_button.png",
                        x_pos=720, y_pos=600)

pause_btn = ToggleButton(command=pause_command,
                         image_path="C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/pause_button.png",
                         x_pos=720, y_pos=600)

skip_btn = Button(command=button_was_pressed,
                  image_path="C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/skip_button.png",
                  x_pos=770, y_pos=600)

previous_btn = Button(command=button_was_pressed,
                      image_path="C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/previous_button.png",
                      x_pos=670, y_pos=600)

playlist_rect = PlaylistDisplay(100, 200, 400, 600)

current_time_txt = Text("0:00", DEFAULT_FONT, (0, 0, 128), 20, 545, 660)

end_time_txt = Text("", DEFAULT_FONT, (0, 0, 128), 20, 905, 660)


def set_time_slider(current_song):
    time_slider.set_song(current_song)
    end_time_txt.set_text(get_song_length_str(current_song.get_song_length()))
    time_slider.draw(screen)


def set_playlist_display():
    playlist_rect.set_playlist_to_text(current_playlist)
    playlist_rect.draw(screen)


def set_buttons(is_paused):
    if is_paused == True:
        play_btn.draw(screen)
    else:
        pause_btn.draw(screen)

    skip_btn.draw(screen)
    previous_btn.draw(screen)


def set_current_song_name_text(song, is_paused):
    font = pygame.font.SysFont(DEFAULT_FONT, 80)
    song_name = font.render(song.get_song_name(), True, (192, 192, 192))
    font = pygame.font.SysFont(DEFAULT_FONT, 30)
    song_author = font.render(song.get_song_author(), True, (192, 192, 192))
    font = pygame.font.SysFont(DEFAULT_FONT, 30)
    if is_paused is True:
        extension = font.render(" is now paused...", True, (192, 192, 192))
    else:
        extension = font.render(" is now playing...", True, (192, 192, 192))

    song_name_rect = song_name.get_rect()
    song_name_rect.center = (750, 140)

    song_author_rect = song_author.get_rect()
    song_author_rect.center = (750, 185)

    extension_rect = extension.get_rect()
    extension_rect.center = (750, 210)

    screen.blit(song_name, song_name_rect)
    screen.blit(extension, extension_rect)
    screen.blit(song_author, song_author_rect)


def init_music_player_window(music_player):
    make_player_circular(music_player)
    current_model = music_player.get_model_head()

    running = True
    play_song(current_model.get_song())

    print(current_model.get_song().get_song_name(), "is now playing...")
    is_song_playing()

    is_pause_song = False

    time.set_timer(pygame.USEREVENT, 1000)

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == SONG_END:
                current_model = current_model.get_next_model()
                play_song(current_model.get_song())
                time_slider.reset_slider()
                print(current_model.get_song().get_song_name(), "is now playing...")

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if is_pause_song is False:
                        pause_song(current_model.get_song())
                        is_pause_song = True
                    elif is_pause_song is True:
                        resume_song(current_model.get_song())
                        is_pause_song = False

                elif event.key == pygame.K_LEFT:
                    current_model = current_model.get_prev_model()
                    play_song(current_model.get_song())
                    print(current_model.get_song().get_song_name(), "is now playing...")
                    time_slider.reset_slider()
                elif event.key == pygame.K_RIGHT:
                    current_model = current_model.get_next_model()
                    play_song(current_model.get_song())
                    print(current_model.get_song().get_song_name(), "is now playing...")
                    time_slider.reset_slider()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                play_btn.set_features(current_model, is_pause_song)
                pause_btn.set_features(current_model, is_pause_song)
                if is_pause_song is False:
                    is_pause_song = pause_btn.get_event(event)
                elif is_pause_song is True:
                    is_pause_song = play_btn.get_event(event)

                if skip_btn.get_event(event):
                    current_model = current_model.get_next_model()
                    play_song(current_model.get_song())
                    print(current_model.get_song().get_song_name(), "is now playing...")
                    is_pause_song = False;
                    time_slider.reset_slider()

                if previous_btn.get_event(event):
                    current_model = current_model.get_prev_model()
                    play_song(current_model.get_song())
                    print(current_model.get_song().get_song_name(), "is now playing...")
                    is_pause_song = False;
                    time_slider.reset_slider()

            elif event.type == pygame.USEREVENT:
                if is_pause_song is False:
                    shift_by_song(time_slider, current_time_txt)
            time_slider.get_event(event)

        draw_window(current_model, is_pause_song)


song_list = get_song_path("SongList")
print(song_list)
playlist = get_playlist(song_list, "Primary")
current_playlist = playlist
'''for song in playlist.get_song_list():
    print(song.get_song_name())'''
#print(playlist.get_song_list())
# print(playlist.get_playlist())

player = shuffle(playlist)

init_music_player_window(player)
