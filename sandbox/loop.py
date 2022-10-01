# Simple pygame program
# Import and initialize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from typing import (
    Tuple
)

# Color constants
WHITE: Tuple[int, int, int] = (255, 255, 255)
BLACK: Tuple[int, int, int] = (0, 0, 0)

if __name__ == "__main__":
    # Run platform dependent intialization
    pygame.init()

    # Define screen resolution in pixels.
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600

    # Set up the drawing window
    screen: pygame.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Run until the user asks to quit
    running: bool = True

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill(BLACK)

        # dRAw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
