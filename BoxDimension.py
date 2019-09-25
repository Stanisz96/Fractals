from PIL import Image
from tkinter import filedialog
import statistics
import math
import matplotlib
import matplotlib.pylab as plt
import numpy



def function_box_dimencion(n, name, file):
    im = Image.open(file)
    out = Image.new('RGB', im.size, 0xffffff)

    width, height = im.size
    w = int(width)
    if  n < 5 : print("Wysokosc: {0} ### Szerokosc: {1}".format(height, width))
    number_squareY: int = height / n


    pixel_group = [0] * (int(number_squareY) + 1)
    nr_in_pixel_group: int = 0
    sum_pixel = [0] * len(pixel_group)
    tab_X = []
    index = 0

    nr_sum_pixel: int = 1

    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = int(statistics.mean([r, g, b]))
            out.putpixel((x, y), (rgb, rgb, rgb))
            if (y % n == 0) and y > 0:
                nr_in_pixel_group += 1
                if rgb < 249:
                    pixel_group[nr_in_pixel_group] += 1
            elif y <= (height - (n - 1)):
                if rgb < 249:
                    pixel_group[nr_in_pixel_group] += 1

        tab_X.append(x)
        for a, val in enumerate(pixel_group):
            sum_pixel[a] += val
            if nr_sum_pixel == n:
                if sum_pixel[a] > 0:
                    for nrx, xval in enumerate(tab_X):
                        for yy in range(n):
                            if (xval < width) and ((yy + a * n) < height):
                                out.putpixel((xval, yy + a * n), (250, 0, 0))
                    index += 1

        if nr_sum_pixel == n:
            sum_pixel = [0] * (len(sum_pixel))

            nr_sum_pixel = 0
            tab_X = []
        nr_sum_pixel += 1

        pixel_group = [0] * len(pixel_group)
        nr_in_pixel_group = 0

    out.save(name)
    return (index, n, w)

def execute_programm(name_file):
    answer = list()
    xarray = []
    yarray = []

    for a,b in zip(range(4,20,2),range(8)):
        answer.append(function_box_dimencion(a, "{0}.png".format(a), name_file))
        print("Obliczenia dla kwadratow o szerokości {0}".format(a))
        yarray.append(math.log10(answer[b][0]))
        xarray.append(math.log10(answer[b][2]/answer[b][1]))

    xarray = numpy.asarray(xarray, dtype=float)
    yarray = numpy.asarray(yarray, dtype=float)
    coefficients = numpy.polyfit(xarray, yarray, 1)
    polynomial = numpy.poly1d(coefficients)
    ys = polynomial(xarray)
    plt.plot(xarray, yarray, 'ro')
    plt.plot(xarray, ys)

    print("Wymiar pudełkowy: {0}".format(coefficients[0]))

    plt.xlabel("Log (1/s)")
    plt.ylabel("Log (N)")
    plt.title("Wymiar pudełkowy")
    plt.show()




if __name__ == '__main__':
    execute_programm('error.png')