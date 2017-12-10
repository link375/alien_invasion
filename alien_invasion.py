import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()

    # import Settings() as alien invasion settings
    ai_settings = Settings()

    # use the ai_settings object to draw a screen
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship and 2 groups to store bullets and aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # check events from the game functions file
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
