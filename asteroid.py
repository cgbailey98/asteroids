from circleshape import CircleShape
from constants import LINE_WIDTH as lw, ASTEROID_MIN_RADIUS as amr
from logger import log_event

import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=lw)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= amr:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            positive_vector = self.velocity.rotate(new_angle)
            negative_vector = self.velocity.rotate(-new_angle)
            new_radius = self.radius - amr
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = positive_vector * 1.2
            asteroid2.velocity = negative_vector * 1.2
