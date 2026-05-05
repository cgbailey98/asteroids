from circleshape import CircleShape
from constants import LINE_WIDTH as lw

import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=(self.x, self.y), radius=self.radius, width=lw)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
