import pygame
import random
from circleshape import CircleShape
import constants as c


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, c.COLOR_WHITE, self.position, self.radius, 2)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()

        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(random_angle)
        vector_b = self.velocity.rotate(-random_angle)
        radius = self.radius - c.ASTEROID_MIN_RADIUS
        x, y = self.position
        asteroid_a = Asteroid(x, y, radius)
        asteroid_a.velocity = vector_a * 1.2
        asteroid_b = Asteroid(x, y, radius)
        asteroid_b.velocity = vector_b * 1.2
