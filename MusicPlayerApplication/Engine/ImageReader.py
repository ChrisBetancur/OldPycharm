from pygame import image
from pygame.sprite import Sprite


class Image(Sprite):
    def __init__(self, image_file, location):
        Sprite.__init__(self)
        self.image = image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location