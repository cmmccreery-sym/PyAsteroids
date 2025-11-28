from circleshape import CircleShape
from logger import log_event
import constants
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            self.position, 
            self.radius, 
            constants.LINE_WIDTH
        )

    def update(self, dt):
        u_vec_with_speed = self.velocity * dt
        self.position += u_vec_with_speed
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            pass
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)

            p_new_vec = self.velocity.copy().rotate(angle)
            n_new_vec = self.velocity.copy().rotate((-1) * angle) 

            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            ast_one = Asteroid(0, 0, new_radius)
            ast_one.position = self.position.copy()

            ast_two = Asteroid(0, 0, new_radius)
            ast_two.position = self.position.copy()

            ast_one.velocity = p_new_vec * 1.2
            ast_two.velocity = n_new_vec * 1.2
