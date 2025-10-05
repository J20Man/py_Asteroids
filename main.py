import pygame
from constants import *
from player import *

def main():

    pygame.init()
    #boilerplate objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #clock
    clock = pygame.time.Clock()
    dt = 0

    #Player objects
    player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    #game loop 
    while True:
        #allows program to be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        #player movement
        player1.update(dt)

        #sets background
        screen.fill("black")
        
        #draws player
        player1.draw(screen)

        #flips screen
        pygame.display.flip()

        #limits fps to 60
        dt = (clock.tick(60) / 1000)



if __name__ == "__main__":
    main()
