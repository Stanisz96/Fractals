import pygame




white = (255,255,255)
black = (0,0,0)


#CONST
WINDOW_SIZE = (600,600)
HALF_SIDE = WINDOW_SIZE[0]/2
POINT1 = (0,0)
POINT2 = (600,0)
POINT3 = (600,600)
POINT4 = (0,600)


def Dywan():
    a = True
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Dywan Sierpińskiego ')
    #pygame.display.iconify()
    # loop until user exits
    gameExit = False
    clock = pygame.time.Clock()
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(black)
        # pygame.draw.polygon(screen, black, [(0,0), (0,600),(600,600),(600,0)])
        add_boxs(0,WINDOW_SIZE[0],screen)
        if a == True:
            pygame.display.update()
            a = False
        else:
            gameExit = True

        clock.tick(10)

    pygame.image.save(screen, "dywan.png")

    pygame.quit()


def add_boxs(iteration, size, surface):

    size = size/3

    # point_1 = [[int(size * (3n+ 1)) for n in range(pow(3,iteration))] for ]
    if size > 1:
        point_1 = [[0 for x in range(pow(3, iteration))] for y in range(pow(3, iteration))]
        point_2 = [[0 for x in range(pow(3, iteration))] for y in range(pow(3, iteration))]
        point_3 = [[0 for x in range(pow(3, iteration))] for y in range(pow(3, iteration))]
        point_4 = [[0 for x in range(pow(3, iteration))] for y in range(pow(3, iteration))]
        for x in range(pow(3, iteration)):
            for y in range(pow(3, iteration)):
                point_1[x][y] = (int(size * (3 * y + 1)), int(size * (3 * x + 1)))
                point_2[x][y] = (int(size * (3 * y + 2)), int(size * (3 * x + 1)))
                point_3[x][y] = (int(size * (3 * y + 2)), int(size * (3 * x + 2)))
                point_4[x][y] = (int(size * (3 * y + 1)), int(size * (3 * x + 2)))
                if size > 1:
                    pygame.draw.polygon(surface, white, [point_1[x][y], point_2[x][y], point_3[x][y], point_4[x][y]])
            pygame.display.update()
        pygame.time.wait(5000)
        add_boxs(iteration+1,size,surface)




if __name__ == '__main__':
    Dywan()
