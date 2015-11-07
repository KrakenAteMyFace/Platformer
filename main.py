import constants
import player
import levels
import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Platformer")
    clock = pygame.time.Clock()

    key = {"l": False,
           "r": False,
           "u": False,
           "d": False}

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key["l"] = True
                elif event.key == pygame.K_RIGHT:
                    key["r"] = True
                elif event.key == pygame.K_UP:
                    key["u"] = True
                elif event.key == pygame.K_DOWN:
                    key["d"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    key["l"] = False
                elif event.key == pygame.K_RIGHT:
                    key["r"] = False
                elif event.key == pygame.K_UP:
                    key["u"] = False
                elif event.key == pygame.K_DOWN:
                    key["d"] = False


        clock.tick(144)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()