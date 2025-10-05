import pygame

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
    

    def collision(self, enemy):
        if self.position.distance_to(enemy.position) <= (self.radius + enemy.radius):
            return True
        return False


