import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Determines the clock for the internal fps
    clock = pygame.time.Clock
    dt = 0

    while True:
    
        # Exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fills the screen with the color black
        screen.fill(0)
        pygame.display.flip()

         # Determines the fps and defines dt taking it as reference
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()