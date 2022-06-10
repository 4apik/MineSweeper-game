import pygame.font


class Buttons:
    def __init__(self, game_settings, screen):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 100, 45
        self.bg_color = game_settings.bg_color
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 40)

        self.prep_images()

    def prep_images(self):
        # Render buttons' images and place them correctly
        # Restart button
        self.restart_image = self.font.render("Restart game", True, self.text_color, self.bg_color)
        self.restart_image_rect = self.restart_image.get_rect()
        self.restart_image_rect.top = self.screen_rect.top
        self.restart_image_rect.left = self.screen_rect.left

    def show_images(self):
        self.screen.blit(self.restart_image, self.restart_image_rect)
