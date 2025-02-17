from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar

class TempConverter:

    def __init__(self):
        self.window = Tk()
        self.window.title("Temperature")
        self.window.geometry("400x400")

        self.main_frame = Frame(self.window)
        self.main_frame.pack(padx = 10, pady =10)

        self.celsius = IntVar()
        self.farenheit = IntVar()
        self.result_c = StringVar()
        self.result_f = StringVar()

    def run(self):
        self.create_widget()
        self.window.mainloop()

    def create_widget(self):
        #c to f
        label_num_1 = Label(
            self.main_frame,
            text = "Converting C to F"
        )
        label_num_1.grid(row=1, column=0, padx=10, pady=5)

        entry_num_1 = Entry(
            self.main_frame,
            width= 20,
            textvariable = self.celsius
        )
        entry_num_1.grid(row=2, column=0, padx=10, pady=5)

        button_num_1 = Button(
            self.main_frame,
            text = "Convert to Farenheit",
            command = self.c_to_f
        )
        button_num_1.grid(row=3, column=0, padx=10, pady=5)

        # f to c
        label_num_2 = Label(
            self.main_frame,
            text = "Converting F to C"
        )
        label_num_2.grid(row=1, column=1, padx=10, pady=5)

        entry_num_2 = Entry(
            self.main_frame,
            width= 20,
            textvariable = self.farenheit
        )
        entry_num_2.grid(row=2, column=1, padx=10, pady=5)

        button_num_2 = Button(
            self.main_frame,
            text = "Convert to Celsius",
            command = self.f_to_C
        )
        button_num_2.grid(row=3, column=1, padx=10, pady=5)

        result_1 = Label(
            self.main_frame,
            textvariable= self.result_f
        )
        result_1.grid(row=4, column=0,padx=10, pady=5)

        result_2 = Label(
            self.main_frame,
            textvariable=self.result_c
        )
        result_2.grid(row=4, column=1, padx=10, pady=5)


    def c_to_f(self):
        celsius = float(self.celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        self.result_f.set(f"C to F is : {fahrenheit}")


    def f_to_C(self):
        farenheit = float(self.farenheit.get())
        celsius = (farenheit - 32) * 5/9
        self.result_c.set(f"F to C is : {celsius}")


def main():
    converter = TempConverter()
    converter.run()

main()