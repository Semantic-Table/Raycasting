import pygame
from player import Player
import math as math

pygame.init()

WHITE = (250,250,250)
BLACK = (30,30,30)
BLUE = (0,0,255)

carryOn = True
tilesize = 40
size = (800,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RayCasting")

clock = pygame.time.Clock()

player = Player(100, 100)

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(player)

carte = [
    '1111111111',
    '1000100001',
    '1000100001',
    '1000000001',
    '1000100001',
    '1000100001',
    '1000100001',
    '1000100001',
    '1000100001',
    '1111111111'
]



def map2D():
    for row in range(10):
        for col in range(10):
            if carte[row][col] == '1':
                pygame.draw.rect(screen, BLACK , [col * tilesize , row * tilesize, tilesize,tilesize])

def movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()
    if keys[pygame.K_UP]:
        player.moveForward()
    if keys[pygame.K_DOWN]:
        player.moveBackward()

while carryOn:
    #close tab
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False
           
    #logic       
    movement()     
    all_sprites_list.update()            
    
    #display
    
    screen.fill(WHITE)
    map2D()
    pygame.draw.line(screen, BLUE, [player.rect.x + 10,player.rect.y + 10], [(player.rect.x + 10)+30*math.sin(player.angle),(player.rect.y + 10)+30*math.cos(player.angle)])
    all_sprites_list.draw(screen)
    pygame.display.flip()
    
    
    clock.tick(60)

pygame.quit()


