import pygame


class Ship():


    def __init__(self, screen):
        """Initialize the ship and set it's starting position"""
        self.screen = screen

        # load the ship image and get it's rect
        self.image = pygame.image.load("images/etherum.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        # define the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        # define the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.centerx += 1


    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)