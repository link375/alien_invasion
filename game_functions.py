import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events"""
    # watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            # check for key presses
        elif event.type == pygame.KEYDOWN:
            # the event is the right arrow key
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    # add the background color
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()