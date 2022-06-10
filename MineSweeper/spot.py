import pygame
import pygame.font
from pygame.sprite import Sprite


class Spot(Sprite):
    """A class to manage mines on the field."""
    def __init__(self, screen, game_settings):
        super(Spot, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game_settings.spot_size, game_settings.spot_size)
        self.color = game_settings.spot_color
        self.bg_color = game_settings.bg_color
        self.value = 0
        self.hidden = True

        # Font settings
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 25)

    def draw_spot(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def show_value(self):
        # Prepare value image and show it on the screen
        self.value_image = self.font.render(str(self.value), True, self.text_color, self.bg_color)
        self.value_image_rect = self.value_image.get_rect()
        self.value_image_rect.center = self.rect.center
        self.screen.blit(self.value_image, self.value_image_rect)
