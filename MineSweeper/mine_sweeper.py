import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from buttons import Buttons
from nn import NN


def main():
    # Initialize pygame, settings, and create a screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("MineSweeper")

    # Make buttons
    buttons = Buttons(game_settings, screen)

    # Make a group of spots
    spots = Group()

    # Create the first minefield
    gf.create_field(screen, game_settings, spots)
    #nn = NN() <- Not working yet
    while True:
        #""" <- Add or remove '#' to swap between two states
        # For humans:
        gf.check_events(screen, game_settings, spots, buttons)
        gf.update_screen(screen, game_settings, spots, buttons)
        """
        # For nn:
        nn.play(game_settings, spots)
        if not game_settings.game_active:
            gf.restart_game(screen, game_settings, spots)
        gf.update_screen(screen, game_settings, spots, buttons)
        #"""

if __name__ == '__main__':
    main()
