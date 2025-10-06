import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        #spawns new smaller asteroid if nec

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rnd_angle = random.uniform(20, 50)

        angle_a = self.velocity.rotate(rnd_angle)
        angle_b = self.velocity.rotate(-rnd_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_a = Asteroid(self.position.x, self.position.y, new_radius)
        ast_a.velocity = angle_a * 1.2
        ast_b = Asteroid(self.position.x, self.position.y, new_radius)
        ast_b.velocity = angle_b * 1.2

