from circleshape import CircleShape
from constants import (PLAYER_RADIUS as pr, LINE_WIDTH as lw, PLAYER_TURN_SPEED as pts, PLAYER_SPEED as ps)

import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, pr)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, color="white", points=self.triangle(), width=lw)
    
    def rotate(self, dt):
        self.rotation += pts * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * ps * dt
        self.position += rotated_with_speed_vector