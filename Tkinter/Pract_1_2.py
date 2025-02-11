from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar
from math import pi

from graphix.graphix import Circle


class Circles:

    def __init__(self):
        self.window = Tk()
        self.window.title("Circle Stuff")
        self.window.geometry("300x300")

        self.main_frame = Frame(self.window)
        self.main_frame.pack(padx = 10, pady =10)

        self.radius = StringVar()

    def run(self):
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        label_num_1 = Label(
            self.main_frame,
            text = "Input Radius in cm:"
        )
        label_num_1.pack()

        input_num_1 = Entry(
            self.main_frame,
            width=20,
            textvariable = self.radius
        )
        input_num_1.pack()


    def circle_circ(self, radius):
        return 2 * pi * radius


    def circ_area(self, radius):
        return pi * radius ** 2


def main():
    circle = Circles()
    circle.run()

main()