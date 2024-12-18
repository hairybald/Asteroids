import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Determines the clock for the internal fps
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    # Nave_triangular
    Nave_triangular = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Espacio = AsteroidField()

   


    while True:
    
        # Exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fills the screen with the color black
        screen.fill("black")

        # Update and draw elements
        for item in drawable:
            item.draw(screen)

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(Nave_triangular):
               print("Game over!")
               return 


        pygame.display.flip()

         # Determines the fps and defines dt taking it as reference
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()