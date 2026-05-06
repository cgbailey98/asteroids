import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH as lw, SHOT_RADIUS as sr

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, sr)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=lw)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
