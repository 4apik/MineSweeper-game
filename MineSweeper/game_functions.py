import pygame, random

from spot import Spot


def check_events(screen, game_settings, spots, buttons):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if any button was clicked
            check_buttons(screen, game_settings, spots, buttons, mouse_x, mouse_y)

            # Else: check if any spot was clicked; open it if yes
            if game_settings.game_active:
                for spot in spots.sprites():
                    if spot.rect.collidepoint(mouse_x, mouse_y):
                        spot.hidden = False
                        # If a mine was clicked - stop the game
                        if spot.value == '*':
                            game_settings.game_active = False


def check_buttons(screen, game_settings, spots, buttons, mouse_x, mouse_y):
    if buttons.restart_image_rect.collidepoint(mouse_x, mouse_y):
        restart_game(screen, game_settings, spots)


def check_adjacency(spot, if_adjacent, game_settings):
    x_adjacency = abs(if_adjacent.rect.x - spot.rect.x)
    y_adjacency = abs(if_adjacent.rect.y - spot.rect.y)
    if x_adjacency <= game_settings.spot_size + 1 and \
            y_adjacency <= game_settings.spot_size + 1 and \
            x_adjacency + y_adjacency != 0:
        return True


def open_zeros(spot, spots, game_settings):
    # Looks for spots with 0 mines around and opens all adjacent spots
    if spot.value == 0:
        for adj_spot in spots.sprites():
            if check_adjacency(spot, adj_spot, game_settings):
                adj_spot.hidden = False


def create_field(screen, game_settings, spots):
    """Fill the screen with spots."""
    # Make one spot and find the number of them in a row
    spot = Spot(screen, game_settings)
    number_spots_x = int(game_settings.screen_width / (spot.rect.width + 1))
    number_spot_rows = int((game_settings.screen_height - 50) / (spot.rect.height + 1))

    # Fill the field with empty spots
    for spot_row in range(number_spot_rows):
        for spot_number in range(number_spots_x):
            create_spot(screen, game_settings, spots, spot_number, spot_row)

    # Assign values to spots
    # Turn random spots into mines
    counter = game_settings.mines_number
    while counter > 0:
        mine_spot = random.choice(spots.sprites())
        if mine_spot.value != '*':
            mine_spot.value = '*'
            counter -= 1

    # Set how many mines each spot has around itself
    for mine in spots.sprites():
        if mine.value == '*':
            for spot in spots.sprites():
                if spot.value != '*':
                    if check_adjacency(mine, spot, game_settings):
                        spot.value += 1


def create_spot(screen, game_settings, spots, spot_number, spot_row):
    """Create a spot and place it correctly."""
    spot = Spot(screen, game_settings)
    spot.rect.x = 1 + ((spot.rect.width + 1) * spot_number)
    spot.rect.y = 50 + ((spot.rect.height + 1) * spot_row)
    spots.add(spot)


def update_screen(screen, game_settings, spots, buttons):
    screen.fill(game_settings.bg_color)
    buttons.show_images()
    for spot in spots.sprites():
        if spot.hidden:
            spot.draw_spot()
        else:
            open_zeros(spot, spots, game_settings)
            spot.show_value()
        # If a mine was clicked - show all mines
        if not game_settings.game_active and spot.value == '*':
            spot.show_value()
    pygame.display.flip()


def restart_game(screen, game_settings, spots):
    # Deletes all spots and creates new ones; make the game active again
    spots.empty()
    create_field(screen, game_settings, spots)
    game_settings.game_active = True
