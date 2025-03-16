from tkinter import Tk, Frame, Label, Button, Toplevel, Entry, IntVar

from SmartLight import SmartLight
from smartHome import SmartHome
from smartPlug import SmartPlug
from smartFridge import SmartFridge

class Editor:
    def __init__(self, index, devices, callback, home):
        super().__init__()
        self.top_window = Toplevel()
        self.top_window.geometry("400x150")
        self.top_frame = Frame(self.top_window)
        self.top_frame.pack(padx=10, pady=10)

        self.input = IntVar() # store whatever the person puts in
        self.index = index
        self.device = devices

        self.smart_home = home

        self.callback = callback
        self.edit_widget(index)

    def edit_widget(self, index):
        for widget in self.top_frame.winfo_children():#delete everything then redraw
            widget.destroy()

        device = self.device[index]
        device_type = type(device).__name__.lower()

        if device_type == "smartfridge":
            device_type = "Fridge"
        elif device_type == "smartlight":
            device_type = "Light"
        elif device_type == "smartplug":
            device_type = "Plug"

        label = Label(
            self.top_frame,
            text="You have selected the: " + device_type
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
            text="Update",
            command=lambda: self.update(device)
        )
        button.grid(row=3, column=0, padx=(80, 0))

        button_1 = Button(
            self.top_frame,
            text="Close",
            command=self.close_window
        )
        button_1.grid(row=4, column=0, padx=(80, 0))

    def update(self, device):
        try:
            new_value = int(self.input.get())

            if isinstance(device, SmartFridge):
                device.temp = new_value
                self.check_error(device.error_message)
            elif isinstance(device, SmartLight):
                device.brightness = new_value
                self.check_error(device.error_message)
            elif isinstance(device, SmartPlug):
                device.consumption_rate = new_value
                self.check_error(device.error_message)
            else:
                print("shits broke")
                return

            device.error_message = ""
            self.callback(self.smart_home)

        except ValueError:
            device.error_message = "Input a Valid integer"

    def check_error(self, message):
        for widget in self.top_frame.winfo_children():#delete the other stuff or it looks bad
            widget.destroy()

        if message == "":
            message = "Device has been updated"
            color = "blue"
        else :
            message = f"Error: {message}"
            color="red"

        message = Label(
            self.top_frame,
            text=message,
            fg= color
        )
        message.grid(row=1, column=0)

        return_button = Button(
            self.top_frame,
            text="Retry",
            command=lambda: self.edit_widget(self.index)
        )
        return_button.grid(row=2,column=0)

        close = Button(
            self.top_frame,
            text="Close",
            command=lambda: self.close_window()
        )
        close.grid(row=3, column=0)


    def close_window(self):
        self.top_window.destroy()
