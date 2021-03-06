import pygame

class Ship():
    """Represent the ship object."""

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set it's starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.moving_up = False
        self.moving_down = False
        # load the ship image and get its rectangle.
        self.image = pygame.image.load('./images/alien.bmp')
        self.img_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen
        self.img_rect.centery = self.screen_rect.centery
        self.img_rect.left = self.screen_rect.left
        # store a decimal value for the ship's center
        self.center = float(self.img_rect.centerx)

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image,self.img_rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_down and self.img_rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_up and self.img_rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # update img_rect from self.center
        self.img_rect.centery = self.center