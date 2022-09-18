import pygame
# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("resources/kitkat.png").convert()
        self.surf = pygame.transform.scale(self.surf, (100,50))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

player = Player()
# Variable to keep the main loop running
running = True


# Main loop

while running:
    # Look at every event in the queue
    for event in pygame.event.get():

        # Did the user hit a key?
        if event.type == KEYDOWN:

            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)
    # Update the displayp
    pygame.display.flip()