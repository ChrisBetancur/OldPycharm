from datetime import datetime

import pygame
import time

from Utilities.Converter import calculate_ratio_milliseconds, get_song_length_str, get_song_length_str
from pygame_ai.colors import WHITE

from music_player_properties.SongPlayer import pause_song, resume_song, play_song, foward_song

DEFAULT_SLIDER_IMG_PATH = "C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/slider.png"
DEFAULT_SLIDER_BUTTON_PATH = "C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/slider_button.png"

DEFAULT_SLIDER_INCREMENT_VALUE = 580


class TimeSlider:
    def __init__(self, x_pos, y_pos):
        self.curr_pos = DEFAULT_SLIDER_INCREMENT_VALUE

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.hit = False
        self.current_song = None

        self.start_time = time.perf_counter()

        self.song_shift = 0

        self.min_val = DEFAULT_SLIDER_INCREMENT_VALUE
        self.max_val = DEFAULT_SLIDER_INCREMENT_VALUE + 300

        self.slider_image = pygame.image.load(DEFAULT_SLIDER_IMG_PATH)
        self.slider_rect = self.slider_image.get_rect()
        self.slider_rect.center = (x_pos, y_pos)

        self.slider_button_image = pygame.image.load(DEFAULT_SLIDER_BUTTON_PATH)
        self.slider_button_rect = self.slider_button_image.get_rect()
        self.slider_button_rect.center = (x_pos, y_pos + 2)
        print(self.slider_button_rect.center)

        # pygame.draw.rect(self.slider_button_image, WHITE, pygame.Rect(10, 30, 80, 5))

    def set_song(self, song):
        self.current_song = song
        self.song_shift = calculate_ratio_milliseconds(self.current_song, self.slider_image)

    def reset_slider(self):
        self.curr_pos = DEFAULT_SLIDER_INCREMENT_VALUE

    def get_event(self, event):
        # shift_by_song(self)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.hit = True
            self.on_click(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.hit = False
        elif event.type == pygame.MOUSEMOTION:
            if self.hit:
                move(self)

    def on_click(self, event):
        if self.slider_button_rect.collidepoint(event.pos):
            move(self)

    def draw(self, surf):
        surf.blit(self.slider_image, self.slider_rect)
        self.slider_button_rect.centerx = self.curr_pos
        surf.blit(self.slider_button_image, self.slider_button_rect)


def shift_by_song(time_slider, current_time_txt):
    time_slider.curr_pos = time_slider.curr_pos + (time_slider.song_shift * 1000)

    curr_seconds = (time_slider.current_song.get_song_length() * (
                time_slider.curr_pos - DEFAULT_SLIDER_INCREMENT_VALUE)) / 300

    # print(curr_seconds)
    current_time_txt.set_text(get_song_length_str(curr_seconds))

    if time_slider.curr_pos < time_slider.min_val:
        time_slider.curr_pos = time_slider.min_val
    if time_slider.curr_pos > time_slider.max_val:
        time_slider.curr_pos = time_slider.max_val


def move(time_slider):
    time_slider.curr_pos = (pygame.mouse.get_pos()[0])

    if time_slider.curr_pos < time_slider.min_val:
        time_slider.curr_pos = time_slider.min_val
    if time_slider.curr_pos > time_slider.max_val:
        time_slider.curr_pos = time_slider.max_val

    offset_value = (time_slider.curr_pos - DEFAULT_SLIDER_INCREMENT_VALUE) / (time_slider.song_shift * 1000)
    # print(offset_value)
    print(offset_value)
    # foward_song(time_slider.current_song, offset_value)


class Button:
    def __init__(self, command, image_path, x_pos, y_pos):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.function = command
        self.is_paused = None

    def set_paused(self, is_paused):
        self.is_paused = is_paused

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.function()
            return True

    def draw(self, surf):
        surf.blit(self.image, self.rect)


def button_was_pressed():
    print("Hit")


class ToggleButton:
    def __init__(self, command, image_path, x_pos, y_pos):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.function = command
        self.current_model = None
        self.is_paused = None

    def set_features(self, current_model, is_paused):
        self.is_paused = is_paused
        self.current_model = current_model

    def set_paused(self, is_paused):
        self.is_paused = is_paused

    def get_event(self, event):
        return self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            return self.function(self.current_model, self.is_paused)
        return self.is_paused

    def draw(self, surf):
        surf.blit(self.image, self.rect)


def play_command(current_model, is_paused):
    if is_paused is True:
        resume_song(current_model.get_song())
        return False
    return True


def pause_command(current_model, is_paused):
    if is_paused is False:
        pause_song(current_model.get_song())
        return True
    return False


class Text:
    def __init__(self, text, font, color, size, x_pos, y_pos):
        self.font = pygame.font.SysFont(font, size)
        self.color = color

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.text_surf = self.font.render(text, True, color)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (x_pos, y_pos)

    def set_text(self, text):
        self.text_surf = None
        self.text_surf = self.font.render(text, True, self.color)

    def uncenter_text(self):
        self.text_rect = (self.x_pos, self.y_pos)

    def draw(self, surf):
        surf.blit(self.text_surf, self.text_rect)


class PlaylistDisplay:
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.width = width
        self.height = height

        self.default_x_pos = x_pos
        self.list_of_song_txt = []

        self.current_playlist = None
        self.s = pygame.Surface((width, height))
        self.s.set_alpha(128)
        self.s.fill((255, 255, 255))

    def set_playlist_to_text(self, playlist):
        self.current_playlist = playlist.get_song_list()
        curr_y_pos = 250
        y_pos_increment = 20

        playlist_name = Text("Playlist name : " + playlist.get_playlist_name(), "Light 300", (0, 0, 0), 40,
                             self.x_pos + (self.width / 2), curr_y_pos - 20)
        self.list_of_song_txt.append(playlist_name)

        for song in self.current_playlist:
            curr_y_pos = curr_y_pos + y_pos_increment
            curr_song = Text(song.get_song_name() + "------" + get_song_length_str(song.get_song_length()), "calibri", (0, 0, 0), 15, (self.x_pos - 155) + (self.width / 2),
                             curr_y_pos)
            curr_song.uncenter_text()
            self.list_of_song_txt.append(curr_song)

    def draw(self, surf):
        # surf.blit(self.playlist_display, self.playlist_display_rect)
        pygame.draw.rect(surf, (0, 0, 0), pygame.Rect(self.x_pos - 1, self.y_pos - 1, self.width + 1, self.height + 1), 2)
        surf.blit(self.s, (self.x_pos, self.y_pos))

        for txt in self.list_of_song_txt:
            txt.draw(surf)
