from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar
from math import pi

class Circles:

    def __init__(self):
        self.window = Tk()
        self.window.title("Circle Stuff")
        self.window.geometry("300x300")

        self.main_frame = Frame(self.window)
        self.main_frame.pack(padx = 10, pady =10)

        self.radius = IntVar()
        self.result = StringVar()
        self.result.set("Answer is: ")

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

        result_1 = Label(
            self.main_frame,
            textvariable=self.result
        )
        result_1.pack()

        button_area = Button(
            self.main_frame,
            text="Area",
            command= self.circ_area()
        )
        button_area.pack(side="left")

        button_circ = Button(
            self.main_frame,
            text="Circumference",
            command=self.circle_circ()
        )
        button_circ.pack(side="left")

        button_close = Button(
            self.main_frame,
            text ="close",
            command= self.window.destroy
        )
        button_close.pack()

    def circle_circ(self):
        radius = float(self.radius.get())
        answer =  2 * pi * radius
        self.result.set(f"Answer is: {answer}")

    def circ_area(self):
        radius = float(self.radius.get())
        answer = pi * radius ** 2
        self.result.set(f"Answer is: {answer}")


def main():
    circle = Circles()
    circle.run()

main()