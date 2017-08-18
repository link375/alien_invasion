import sys
import pygame
from settings import Settings

def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()
    # import Settings() as alien invasion settings
    ai_settings = Settings()
    # use the ai_settings object to draw a screen
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height ))
    pygame.display.set_caption("Alien Invasion")


    # Start the main loop for the game.
    while True:

        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        # add the background color
        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()