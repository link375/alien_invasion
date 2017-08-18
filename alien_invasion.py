import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()
    # import Settings() as alien invasion settings
    ai_settings = Settings()
    # use the ai_settings object to draw a screen
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height ))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        #check events from the game functions file
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()