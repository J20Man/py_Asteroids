import pygame
from constants import *

#Class for the in game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        #leave blank to allow children to overwrite
        pass

    def update(self, dt):
        #as above, children will overwrite
        pass




def main():

    pygame.init()
    #boilerplate objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #clock
    clock = pygame.time.Clock()
    dt = 0

    #game loop 
    while True:
        #allows program to be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("BLACK")
        pygame.display.flip

        #limits fps to 60
        dt = (clock.tick(60) / 1000)



if __name__ == "__main__":
    main()
