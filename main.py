from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
import sys


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    game_screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    
    
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        game_screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

            for shot in shots:
                log_event("asteroid_shot")
                if obj.collides_with(shot):
                    shot.kill()
                    obj.split()

        for obj in drawable:
            obj.draw(game_screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
