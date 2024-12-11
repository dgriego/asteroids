import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
import constants as c
from player import Player
from shot import Shot


def main():
    x = c.SCREEN_WIDTH
    y = c.SCREEN_HEIGHT
    pygame.init()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    # setup
    screen = pygame.display.set_mode((x, y))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x / 2, y / 2)
    asteroidField = AsteroidField()

    print("Starting asteroids!")

    while True:
        screen.fill(c.COLOR_BLACK)

        for item in drawable:
            item.draw(screen)

        dt = clock.tick(60) / 1000

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

        # render/update contents of the entire display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
