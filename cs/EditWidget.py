from tkinter import Tk, Frame, Label, Button, Toplevel, Entry, IntVar

from coursework.smartFridge import SmartFridge


class Editor:
    def __init__(self, parent, index, devices):
        super().__init__()
        self.top_window = Toplevel()
        self.top_window.geometry("300x300")
        self.top_frame = Frame(self.top_window)
        self.top_frame.pack(padx=10, pady=10)

        self.input = IntVar() # store whatever the person puts in

        self.edit_widget(index, devices)

    def edit_widget(self, index, devices):
        device = devices[index]

        device_type = type(device).__name__.lower()

        if device_type == "smartfridge":
            device_type = "Fridge"
        elif device_type == "smartlight":
            device_type = "Light"
        elif device_type == "smartplug":
            device_type = "Plug"

        label= Label(
            self.top_frame,
            text = "You have selected the: " + device_type
        )
        label.grid(row=0, column=0)

        entry_num1 = Entry(
            self.top_frame,
            width=20,
            textvariable=self.input
        )
        entry_num1.grid(row=1, column=0)

        button = Button(
            self.top_frame,
            text = "Update",
            command=lambda: self.set_temp(device)
        )
        button.grid(row=2, column=1)


        print(device)


    def set_temp(self, device):
        new_temp = self.input.get()
        if isinstance(device, SmartFridge):
            device.temp= new_temp
        else:
            print("wrong device")









