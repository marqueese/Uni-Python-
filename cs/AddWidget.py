from tkinter import Toplevel, Frame, Label, Button

from SmartLight import SmartLight
from smartFridge import SmartFridge
from smartPlug import SmartPlug


class AddWidget:
    def __init__(self, parent, devices, smart_home, callback):
        super().__init__()
        self.parent = parent
        self.devices = devices
        self.smart_home = smart_home
        self.callback = callback
        self.add_widget_window = None
        self.add_widget()

    def add_widget(self):
        self.add_widget_window = Toplevel(self.parent)
        self.add_widget_window.geometry("350x100")
        top_frame_2 = Frame(self.add_widget_window)
        top_frame_2.pack(padx=10, pady=10)

        label = Label(
            top_frame_2,
            text="What item do you want to add",
            highlightbackground="black",
            highlightthickness=3
        )
        label.grid(row=0, column=1)

        plug_button = Button(
            top_frame_2,
            text="Add Plug",
            width=9,
            relief="raised",
            borderwidth=3,
            command=self.add_plug
        )
        plug_button.grid(row=1, column=0)

        fridge_button = Button(
            top_frame_2,
            text="Add Fridge",
            width=9,
            relief="raised",
            borderwidth=3,
            command=self.add_fridge
        )
        fridge_button.grid(row=1, column=1)

        light_button = Button(
            top_frame_2,
            text="Add Light",
            width=9,
            relief="raised",
            borderwidth=3,
            command=self.add_light
        )
        light_button.grid(row=1, column=2)

    def add_plug(self):
        plug_1 = SmartPlug(75)
        self.smart_home.add_devices(plug_1)
        #self.devices.append(plug_1) <-- this breaks stuff
        self.callback()
        self.add_widget_window.destroy()

    def add_light(self):
        light_1 = SmartLight(28)
        self.smart_home.add_devices(light_1)
        #self.devices.append(light_1)
        self.callback()
        self.add_widget_window.destroy()

    def add_fridge(self):
        fridge_1 = SmartFridge(3)
        self.smart_home.add_devices(fridge_1)
        #self.devices.append(fridge_1)
        self.callback()
        self.add_widget_window.destroy()

