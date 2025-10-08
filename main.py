import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from menu import show_difficulty_menu


def main():

    pygame.init()
    #boilerplate objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    difficulty = show_difficulty_menu(screen)
    print(f"Selected difficulty: {difficulty}")

    if difficulty == "easy":
        AsteroidField.asteroid_count = 5
    elif difficulty == "medium":
        AsteroidField.asteroid_count = 10
    elif difficulty == "hard":
        AsteroidField.asteroid_count = 15

        
    #clock
    clock = pygame.time.Clock()
    
    #player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (drawable, updatable, shots)
    Ast_field = AsteroidField()
    
    
    #Player objects
    player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    
    dt = 0

    #game loop 
    while True:
        #allows program to be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        #player movement
        updatable.update(dt)
        #checks collision
        for obj in asteroids:
            if player1.collision(obj) == True:
                print("Game Over!")
                sys.exit()
            elif player1.collision(obj) == False:
                pass
        for obj in asteroids:
            for shot in shots:
                if shot.collision(obj):
                    shot.kill()
                    obj.split()

        #sets background
        screen.fill("black")
        
        #draws player
        for obj in drawable:
            obj.draw(screen)

        #flips screen
        pygame.display.flip()

        #limits fps to 60
        dt = (clock.tick(60) / 1000)



if __name__ == "__main__":
    main()
