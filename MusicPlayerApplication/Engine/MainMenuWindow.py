import pygame, sys, os
import pygame_gui

from Engine.ImageReader import Image

from GUI import Button, button_was_pressed

(WIDTH, HEIGHT) = (1500, 1000)
(r, g, b) = (0, 0, 0)
DEFAULT_FONT = "Light 300"

background = Image("C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/background.jpg", [-85, 0])

# background_image = pygame.image.load("C:/Users/chris/PycharmProjects/MusicPlayerApplication/background.jpg")

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((r, g, b))
pygame.display.flip()
shuffle_button = pygame.image.load("C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/button_shuffle.png")

#shuffle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text = "Shuffle", manager = manager)

play_btn = Button(command=button_was_pressed, image_path="C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/play_button.png", x_pos = 500, y_pos = 400)
pause_btn = Button(command=button_was_pressed, image_path="C:/Users/chris/PycharmProjects/MusicPlayerApplication/Images/pause_button.png", x_pos = 500,y_pos = 350)

def draw_window():
    screen.fill((r, g, b))
    screen.blit(background.image, background.rect)
    play_btn.draw(screen)
    pause_btn.draw(screen)

def init_main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            play_btn.get_event(event)
            pause_btn.get_event(event)
        draw_window()
        pygame.display.update()


init_main_menu()
