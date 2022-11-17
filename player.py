import pygame
import math as math

WHITE = (0,0,0)
GREY = (100,100,100)

class Player(pygame.sprite.Sprite):
    def __init__(self, posX , posY):
        super().__init__()
        
        self.angle = 0
        
        self.image = pygame.Surface([20,20])
        self.image.fill(GREY)
        self.image.set_colorkey(GREY)
        
        pygame.draw.rect(self.image, (230,20,20), [0,0,20,20])
        
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        
        
    def moveLeft(self):
        self.angle += 0.05
        
    def moveRight(self):
        self.angle -= 0.05
        
    def moveForward(self):
        self.rect.x += math.sin(self.angle) * 5
        self.rect.y += math.cos(self.angle) * 5
    
    def moveBackward(self):
        self.rect.x -= math.sin(self.angle) * 5
        self.rect.y -= math.cos(self.angle) * 5
        