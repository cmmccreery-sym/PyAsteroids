import constants
import pygame
from shot import Shot
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate((-1) * dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move((-1) * dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.cooldown_timer -= dt


    def shoot(self, dt):
        if self.cooldown_timer > 0:
            pass
        else:
            shot = Shot(0, 0, 0)
            shot.position = self.position.copy()

            u_vec = pygame.math.Vector2(0, 1)
            r_vec = u_vec.rotate(self.rotation)
            shot.velocity = r_vec * constants.PLAYER_SHOOT_SPEED
            self.cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS


    def move(self, dt):
        u_vec = pygame.math.Vector2(0, 1)
        r_vec = u_vec.rotate(self.rotation)
        r_vec_with_speed = r_vec * constants.PLAYER_SPEED * dt
        self.position += r_vec_with_speed
        


