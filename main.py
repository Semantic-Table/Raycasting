import pygame
from player import Player
import math as math

pygame.init()

WHITE = (250, 250, 250)
BLACK = (30, 30, 30)
BLUE = (0, 0, 255)
SKY = (40,50,60)
GROUND = (50,105,50)
RED = (255, 0, 0)

carryOn = True
tilesize = 40
size = (800, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RayCasting")

mapsize = 10
precision = 20
fov = 120 * (math.pi / 180)  # fov is rays casted in radiant
rays = int(size[0])  # its the fov in degrees
startRect = 0 # size[0]/2
renderWidth = size[0] # size[0]/2
debug = True


if debug:
    renderWidth = size[0]/2
    startRect = size[0]/2
    rays = int(size[0]/2)





clock = pygame.time.Clock()

player = Player(100, 100)

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(player)

carte = [
    '1111111111',
    '1000100001',
    '1000100001',
    '1000000001',
    '1000111011',
    '1000100001',
    '1000100001',
    '1000100001',
    '1000100001',
    '1111111111'
]


def calcPosX(ray, depth, startAngle):
    return (player.rect.x + 10) + ((tilesize/precision) * depth) * (math.sin(player.angle - fov/2 + (fov/rays * ray)))


def calcPosY(ray, depth, startAngle):
    return (player.rect.y + 10) + ((tilesize/precision) * depth) * (math.cos(player.angle - fov/2 + (fov/rays * ray)))


def renderRayCast():
    startAngle = fov/2
    for ray in range(rays):
        for depth in range(mapsize * precision):
            dotX = calcPosX(ray, depth, startAngle)
            dotY = calcPosY(ray, depth, startAngle)
            if debug:
                circle = pygame.draw.circle(screen, RED, [calcPosX(ray, depth, startAngle), calcPosY(ray, depth, startAngle)], 2)
            if carte[int(dotY/40)][int(dotX/40)] != '0':
                pygame.draw.rect(screen, [depth/2,depth/2,depth/2], [size[0] - (ray * renderWidth/(rays-1)) ,(size[1] - ((size[1]*2) /(depth + 1)))/2,renderWidth/rays+1,(size[1]*2)/(depth+1)])
                break


def map2D():
    for row in range(10):
        for col in range(10):
            if carte[row][col] == '1':
                pygame.draw.rect(
                    screen, BLACK, [col * tilesize, row * tilesize, tilesize, tilesize])


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
    # close tab
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    # logic
    movement()
    all_sprites_list.update()

    # display

    screen.fill(WHITE)
    if debug:
        map2D()
        
    pygame.draw.rect(screen, BLUE, [startRect,0,renderWidth,size[1]/2])
    pygame.draw.rect(screen, GROUND, [startRect,size[1]/2,renderWidth,size[1]/2])
    renderRayCast()
    
    if debug:
        all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
