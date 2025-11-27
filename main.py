from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import pygame

def main():
    pygame.init()
    game_screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        game_screen.fill("black")
        pygame.display.flip()



if __name__ == "__main__":
    main()
