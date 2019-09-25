import time
import matplotlib
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

try:
    from PIL import Image
except:
    import Image
from PIL import ImageTk, ImageSequence

from BoxDimension import execute_programm
from Carpet import Dywan
from SnowFlake import Snow
from Triangle import Trojkat


class App:
    def __init__(self,parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=600, height=200)
        self.canvas.grid(row=0,columnspan=2)
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                        "title_fraktale.gif"))]
        self.image = self.canvas.create_image(300,100,image=self.sequence[0])
        self.animating = True
        self.animate(0)
    def animate(self, counter):
        time.sleep(0.05)
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        if not self.animating:
            return

        self.parent.after(20, lambda: self.animate((counter+1) % (len(self.sequence)-1)))


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def change_disabled():
    if SniezkaWindow.has_been_called:
        label_snow_box.config(state="normal")
        label_snow_box.update()
        SniezkaWindow.has_been_called = False
    else:
        print("ERROR")

def spr():
    print("Sniezka {0}".format(SniezkaWindow.has_been_called))
    print("Trojkat {0}".format(TrojkatWindow.has_been_called))
    print("Dywan {0}".format(DywanWindow.has_been_called))

def close_window(close):
    close.destroy()

def choose_box_program():
    if SniezkaWindow.has_been_called:
        SniezkaWindow.has_been_called = False
        execute_programm('sniezka.png')
    if TrojkatWindow.has_been_called:
        TrojkatWindow.has_been_called = False
        execute_programm('trojkat.png')
    if DywanWindow.has_been_called:
        DywanWindow.has_been_called = False
        execute_programm('dywan.png')
    else:
        messagebox.showwarning("Uwaga!", "Najpierw stwórz fraktala :)")

class SniezkaWindow:

    def __init__(self):
        SniezkaWindow.has_been_called = True
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        self.img = mpimg.imread('sniezka.png')
        self.imgplot = plt.imshow(self.img)
        self.imgplot.axes.get_xaxis().set_visible(False)
        self.imgplot.axes.get_yaxis().set_visible(False)
        plt.show()
        #change_disabled()
SniezkaWindow.has_been_called = False

class TrojkatWindow:

    def __init__(self):
        TrojkatWindow.has_been_called = True
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        self.img = mpimg.imread('trojkat.png')
        self.imgplot = plt.imshow(self.img)
        self.imgplot.axes.get_xaxis().set_visible(False)
        self.imgplot.axes.get_yaxis().set_visible(False)
        plt.show()
TrojkatWindow.has_been_called = False

class DywanWindow:

    def __init__(self):
        DywanWindow.has_been_called = True
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        self.img = mpimg.imread('dywan.png')
        self.imgplot = plt.imshow(self.img)
        self.imgplot.axes.get_xaxis().set_visible(False)
        self.imgplot.axes.get_yaxis().set_visible(False)
        plt.show()
DywanWindow.has_been_called = False

class IFSWindow:

    def __init__(self):
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        from IFS import IFS_function

        def choose_name(choose):
            IFS_function(choose)
            img = mpimg.imread('ifs.png')
            imgplot = plt.imshow(img)
            imgplot.axes.get_xaxis().set_visible(False)
            imgplot.axes.get_yaxis().set_visible(False)
            plt.show()


        self.root3 = Tk()
        self.root3.title("IFS")
        self.root3.wm_iconbitmap('icon2.ico')
        self.root3.geometry('100x180')
        self.root3.resizable(False, False)
        self.frame = Frame(self.root3)
        self.frame.pack()
        #buttons
        self.bush_button = Button(self.frame,height=1, width=12, text="Krzak", command= lambda: choose_name('bush'))
        self.dragon_button = Button(self.frame,height=1, width=12, text="Smok", command=lambda: choose_name('dragon'))
        self.fern_button = Button(self.frame,height=1, width=12, text="Paproć", command=lambda: choose_name('fern'))
        self.c_button = Button(self.frame,height=1, width=12, text="C Fraktal", command=lambda: choose_name('c'))
        self.triangle_button = Button(self.frame,height=1, width=12, text="Trójkąt", command=lambda: choose_name('triangle'))
        self.random_button = Button(self.frame,height=1, width=12, text="Losowy", command=lambda: choose_name('random'))
        self.exit_button = Button(self.frame, height=1, width=12, text="WYJŚCIE",command=lambda: close_window(self.root3))

        #button pack
        self.bush_button.pack()
        self.dragon_button.pack()
        self.fern_button.pack()
        self.c_button.pack()
        self.triangle_button.pack()
        self.random_button.pack()
        self.exit_button.pack()

        self.root3.mainloop()

root = Tk()

root.title("Fraktale")
root.wm_iconbitmap('icon2.ico')
root.geometry('600x500')
root.resizable(False, False)

a= App(root)

frame1 = Frame(root,highlightbackground="#13a380", highlightthickness=1,bd=5)
frame1.grid(row=1)
frame2 = Frame(root,highlightbackground="#13a380", highlightthickness=1,bd=5)
frame2.grid(row=1,column=1)
frame3 = Frame(root,highlightbackground="#13a380", highlightthickness=1,bd=5)
frame3.grid(row=2,columnspan=2)
frame4 = Frame(root,highlightbackground="#13a380", highlightthickness=1,bd=5)
frame4.grid(row=3)
frame5 = Frame(root,highlightbackground="#13a380", highlightthickness=1,bd=5)
frame5.grid(row=3,column=1)


helv16 = font.Font(family='Helvetica', size=16, weight=font.BOLD)
helv12 = font.Font(family='Helvetica', size=12, weight=font.BOLD)



label_snow_box = Button(frame1, text="Box dimension", command=choose_box_program)
label_snow = Button(frame1, text="Śnieżka Kocha",bg="red", activebackground="red", command=combine_funcs(Snow,SniezkaWindow),)
label_trojkat_box = Button(frame2, text="Box dimension", command=choose_box_program)
label_trojkat = Button(frame2, text="Trójkąt Sierpińskiego", bg="turquoise", activebackground="turquoise", command=combine_funcs(Trojkat,TrojkatWindow))
label_dywan_box = Button(frame3, text="Box dimension", command=choose_box_program)
label_dywan = Button(frame3, text="Dywan Sierpińskiego", bg="yellow", activebackground="yellow", command=combine_funcs(Dywan,DywanWindow))
label_ifs = Button(frame4, text="IFS", bg="green", activebackground="green",font=helv12, command=IFSWindow)
label_exit = Button(frame5, text="WYJŚCIE", bg="pink", activebackground="pink", font=helv16, command= lambda: close_window(root))




label_snow.grid(row=0,column=2, ipadx=2,ipady=8)
label_snow_box.grid(row=1,column=2)
label_trojkat.grid(row=0, column=1, ipady=8)
label_trojkat_box.grid(row=1,column=1, ipadx=16)
label_dywan.grid(row=1,columnspan=2, ipady=8)
label_dywan_box.grid(row=2,columnspan=2, ipady=3, ipadx=16)
label_ifs.grid(row=3,ipadx=20,ipady=4)
label_exit.grid(row=3, column=1)


root.mainloop()