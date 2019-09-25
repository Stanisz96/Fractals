from tkinter import *
import pygame
import numpy as np
from math import pi
from PIL import Image, ImageTk


white = (255,255,255)
black = (0,0,0)





#CONST
WINDOW_SIZE = [600,600]
HALF_SIDE = WINDOW_SIZE[0]/2


def Snow():
    a = True
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Krzywa Kocha')
    #pygame.display.iconify()
    # loop until user exits
    gameExit = False
    clock = pygame.time.Clock()
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        screen_center = np.array([WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2])
        #setting Kochs_curve
        kochs_curve_top = screen_center + vector(HALF_SIDE, pi/2)
        kochs_curve_left = screen_center + vector(HALF_SIDE, pi/2 + 2*pi/3)
        kochs_curve_right = screen_center + vector(HALF_SIDE, pi/2 + 4*pi/3)

        #drawing Kochs curve
        draw_line(screen, kochs_curve_top, kochs_curve_left)
        pygame.display.update()
        pygame.time.wait(5000)
        draw_line(screen, kochs_curve_left, kochs_curve_right)
        pygame.display.update()
        pygame.time.wait(5000)
        draw_line(screen, kochs_curve_right, kochs_curve_top)

        if a == True:
            pygame.display.update()
            a = False
        else:
            gameExit = True

        clock.tick(10)

    pygame.image.save(screen, "sniezka.png")

    pygame.quit()




def vector(size, angle):
    return size * np.array([np.cos(angle),np.sin(angle)])

def img_window(file):
    root = Tk()
    image = Image.open(file)
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.image = photo
    label.pack()
    root.mainloop()

def draw_line(screen, start_line, end_line):
    if np.linalg.norm( end_line - start_line ) / 3 < 1:
        pygame.draw.line(screen, [0,0,0], start_line, end_line, 1)
    else:
        #find normal
        line_normal = np.array([end_line[1] - start_line[1], start_line[0] - end_line[0]])
        #find three points of triangle
        triangle_left = 2/3 * start_line + 1/3 * end_line  # 1/3 of this line
        triangle_right = 1/3 * start_line + 2/3 * end_line  # 2/3 of this line
        triangle_top = 1/2 * start_line + 1/2 * end_line + np.sqrt(3) / 2 / 3 * line_normal #top
        #recurse for every triangle
        draw_line(screen, start_line,     triangle_left)
        draw_line(screen, triangle_left,  triangle_top)
        draw_line(screen, triangle_top,   triangle_right)
        draw_line(screen, triangle_right, end_line)
        pygame.display.update()

if __name__ == '__main__':
    Snow()
