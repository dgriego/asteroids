import pygame
import constants as c


def main():
    pygame.init()
    surface = pygame.display.set_mode((c.SCREEN_HEIGHT, c.SCREEN_WIDTH))
    print("Starting asteroids!")

    while True:
        surface.fill(c.COLOR_BLACK)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
