import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Creating radius of new split asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Creating the new split asteroids with current position and new radii
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Creating the new angles of the velocity vectors for the new split asteroids
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)        

        #Setting velocity of the new asteroids
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)