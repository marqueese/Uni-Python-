from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar

class TempDecision:

    def __init__(self):
        self.window = Tk()
        self.window.title("what to do")
        self.window.geometry("300x400")

        self.main_frame = Frame(self.window)
        self.main_frame.pack(padx = 10, pady =10)

        self.temp = IntVar()
        self.decision = StringVar()


    def run(self):
        self.create_widget()
        self.window.mainloop()

    def create_widget(self):
        label_num_1 = Label(
            self.main_frame,
            text = "What is the temp today?\nin C"
        )
        label_num_1.pack()

        entry_num_1 = Entry(
            self.main_frame,
            width= 20,
            textvariable = self.temp
        )
        entry_num_1.pack()

        button_num_1 = Button(
            self.main_frame,
            text = "Decide what to do",
            command = self.temp_choice
        )
        button_num_1.pack()

        result_1 = Label(
            self.main_frame,
            textvariable= self.decision
        )
        result_1.pack()


    def temp_choice(self):
        temp = float(self.temp.get())

        if temp > 50:
            self.decision.set("You're dead just accept it")
        elif temp > 25:
            self.decision.set("Go for a swim in the sea")
        elif 10 <= temp <= 25:
            self.decision.set("Go shopping in Gunwharf Quays")
        elif temp < 10:
            self.decision.set("Stay indoors and watch a film")

def main():
    temp = TempDecision()
    temp.run()

main()