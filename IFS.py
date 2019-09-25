import matplotlib
import random
import pygame
import numpy as np




XFORM_MATRIX = []


xy_position = [0,0]
new_xy = []


white = (255,255,255)
black = (0,0,0)


#CONST
WINDOW_SIZE = (600,600)



def IFS_function(choosed):
    global XFORM_MATRIX
    global xy_position
    number_of_iterations = 0

    if choosed is 'bush':
        XFORM_MATRIX = [[-0.67, -0.02, -0.18, 0.81, 0, 1.02],
                            [0.40, 0.40, -0.10, 0.40, -0.04, 0.06],
                            [-0.40, -0.40, -0.10, 0.40, 0.04, 0.06],
                            [-0.10, 0.0, 0.44, 0.44, 0.00, -0.14]]
        number_of_iterations = 1000000
        print(XFORM_MATRIX)
    if choosed is 'dragon':
        XFORM_MATRIX = [[0.824074, 0.281428, -0.212346, 0.864198, -1.882290, -0.110607],
                        [0.088272, 0.520988, -0.463889, -0.377778, 0.785360, 8.095795]]
        number_of_iterations = 200000
        print(XFORM_MATRIX)
    if choosed is 'fern':
        XFORM_MATRIX = [[0.85, 0.04, -0.04, 0.85, 0, 1.6],
                        [-0.15, 0.28, 0.26, 0.24, 0, 0.44],
                        [0.20, -0.26, 0.23, 0.22, 0, 1.6],
                        [0, 0, 0, 0.16, 0, 0]]
        number_of_iterations = 200000
        print(XFORM_MATRIX)
    if choosed is 'c':
        XFORM_MATRIX = [[0.5, -0.5, 0.5, 0.5, 0.0, 0.0],
                    [0.5, 0.5, -0.5, 0.5, 0.5, 0.5]]
        number_of_iterations = 200000
        print(XFORM_MATRIX)
    if choosed is 'triangle':
        XFORM_MATRIX = [[0.5, 0, 0, 0.5, 0.0, 0.0],
                        [0.5, 0, 0, 0.5, 0.0, 0.5],
                        [0.5, 0, 0, 0.5, 0.5, 0.5]]
        number_of_iterations = 300000
        print(XFORM_MATRIX)
    if choosed is 'random':
        XFORM_MATRIX = [[round(random.uniform(-0.8,0.8),5), round(random.uniform(-0.8,0.8),5), round(random.uniform(-0.8,0.8),5),
                         round(random.uniform(-0.8, 0.8), 5), round(random.uniform(-0.8,0.8),5), round(random.uniform(-0.8,0.8),5)],
                        [round(random.uniform(-0.8, 0.8), 5), round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5), round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5)],
                        [round(random.uniform(-0.8, 0.8), 5), round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5), round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5)],
                        [round(random.uniform(-0.8, 0.8), 5), round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5), round(random.uniform(-0.8, 0.8), 5),
                         round(random.uniform(-0.8, 0.8), 5)]]
        number_of_iterations = 500000
        print(XFORM_MATRIX)



    a = True
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('IFS ')
    pygame.display.iconify()
    # loop until user exits
    gameExit = False
    clock = pygame.time.Clock()
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        for a in range(number_of_iterations):
            iteration_function(xy_position, screen, choosed)


        pygame.time.wait(1000)
        if a == True:
            pygame.display.update()
            a = False

        else:
            gameExit = True

        clock.tick(10)
    pygame.transform.rotate(screen, 90)
    pygame.image.save(screen, "ifs.png")
    original_image = pygame.image.load("ifs.png").convert()
    if choosed is 'triangle':
        original_image = pygame.transform.rotate(original_image, 0)
    else:
        original_image = pygame.transform.rotate(original_image, 180)
    pygame.image.save(original_image, "ifs.png")
    pygame.quit()





def iteration_function(xy, surface,choosed):
    # global array_of_points
    global xy_position

    # print(xy_position)
    if choosed is 'bush':
        xy_position = xy_function(random.randint(0,3), xy[0], xy[1])
        x = int(140*xy_position[0] + 300)
        y = int(140*xy_position[1] - 10)
    if choosed is 'dragon':
        xy_position = xy_function(np.random.choice((0, 1), p=[0.8, 0.2]), xy[0], xy[1])
        x = int(45 * xy_position[0] + 300)
        y = int(45 * xy_position[1] + 100)
    if choosed is 'fern':
        xy_position = xy_function(np.random.choice((0, 1, 2, 3), p=[0.85, 0.07, 0.07, 0.01]), xy[0], xy[1])
        x = int(50 * xy_position[0] + 300)
        y = int(50 * xy_position[1] + 40)
    if choosed is 'random':
        xy_position = xy_function(random.randint(0,3), xy[0], xy[1])
        x = int(200 * xy_position[0] + 300)
        y = int(200 * xy_position[1] + 300)
    if choosed is 'c':
        xy_position = xy_function(random.randint(0,1), xy[0], xy[1])
        x = int(140*xy_position[0] + 200)
        y = int(140*xy_position[1] + 280)
    if choosed is 'triangle':
        xy_position = xy_function(random.randint(0,2), xy[0], xy[1])
        x = int(450*xy_position[0] + 140)
        y = int(450*xy_position[1] + 10)

    # print(x)
    # print(y)
    surface.set_at([x,y], black)



def xy_function(choosed_affine_transformation, x, y):
    global XFORM_MATRIX
    n = choosed_affine_transformation

    return XFORM_MATRIX[n][0]*x + XFORM_MATRIX[n][1]*y + XFORM_MATRIX[n][4],\
           XFORM_MATRIX[n][2]*x + XFORM_MATRIX[n][3]*y + XFORM_MATRIX[n][5]






if __name__ == '__main__':
    IFS_function('triangle')
