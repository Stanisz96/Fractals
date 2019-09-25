import pygame
from pygame import gfxdraw
import random


white = (255,255,255)
black = (0,0,0)



#CONST
WINDOW_SIZE = [800,800]
HALF_SIDE = WINDOW_SIZE[0]/2
POINT_1 = [50,700]
POINT_2 = [400,100]
POINT_3 = [750,700]
START_POINT = [400,400]

def Trojkat():
    a = True
    current_position = [0,0]
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Trojkat Sierpinskiego ')
    # loop until user exits
    gameExit = False
    clock = pygame.time.Clock()
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        for a in range(0,200000):
            choosed_point = choose_point()
            if a == 0:
                current_position = START_POINT
                gfxdraw.pixel(screen, START_POINT[0], START_POINT[1], white)
                current_position = [int((x+y)/2) for x,y in zip(current_position,choosed_point)]
                gfxdraw.pixel(screen, current_position[0], current_position[1], white)
            else:
                current_position = [int((x+y)/2) for x, y in zip(current_position, choosed_point)]
                gfxdraw.pixel(screen, current_position[0], current_position[1], black)
            if a == 50000 or a == 100000:
                pygame.display.update()
                pygame.time.wait(4000)
        pygame.time.wait(100)

        if a == True:
            pygame.display.update()
            a = False
        else:
            gameExit = True

        clock.tick(10)

    pygame.image.save(screen, "trojkat.png")

    pygame.quit()

def choose_point():
    rnd = random.randint(1,3)
    if rnd == 1:
        return POINT_1
    if rnd == 2:
        return POINT_2
    if rnd == 3:
        return POINT_3



if __name__ == '__main__':
    Trojkat()
