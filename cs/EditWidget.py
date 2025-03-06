from tkinter import Tk, Frame, Label, Button, Toplevel, Entry, IntVar
from smartFridge import SmartFridge

class Editor:
    def __init__(self, index,error_message , devices, callback):
        super().__init__()
        self.top_window = Toplevel()
        self.top_window.geometry("300x150")
        self.top_frame = Frame(self.top_window)
        self.top_frame.pack(padx=10, pady=10)

        self.input = IntVar() # store whatever the person puts in
        self.index = index
        self.devices = devices

        self.callback = callback
        self.edit_widget(index)
        self.error_message = error_message

    def edit_widget(self, index):
        device = self.devices[index]

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
            command=lambda: self.update(device_type)
        )
        button.grid(row=2, column=0,padx=(80, 0))

        button_1 = Button(
            self.top_frame,
            text="Close",
            command=self.close_window
        )
        button_1.grid(row=3, column=0, padx=(80, 0))

    def error_message(self):
        if self.error_message != "":
            exit()
        else:
            pass




    def update(self, device_type):
        print(self.error_message)

        new_value = self.input.get()
        device = self.devices[self.index]

        if device_type == "Fridge":
            device.temp = new_value
        elif device_type == "Light":
            device.brightness = new_value
        elif device_type == "Plug":
            device.consumption_rate = new_value

        self.callback()
        self.close_window()

    def close_window(self):
        self.top_window.destroy()

