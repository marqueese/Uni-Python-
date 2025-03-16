from tkinter import Tk, Frame, Label, Button, StringVar, OptionMenu,Entry
from SmartLight import SmartLight
from SmartHomesApp import SmartHomeApp
from smartFridge import SmartFridge
from smartPlug import SmartPlug
from smartHome import SmartHome
from EditWidget import Editor
from AddWidget import AddWidget

class SmartHomeGUI:

    def __init__(self, app: SmartHomeApp):
        super().__init__()
        self.app = app
        self.window = Tk()
        self.window.title("Smart Home GUI")
        self.window.geometry("600x400")

        #coloring and frame
        self.window.configure(bg="lightblue", borderwidth=3, highlightbackground="black") # use configure to alter the background elements
        self.main_frame = Frame(self.window)
        self.main_frame.pack(padx=10, pady=10)

        self.smart_home = SmartHome("Test")
        self.editor = Editor

        self.home_delete_error = StringVar()

        self.home_name = StringVar()
        if self.app.smart_homes:
            self.home_name.set(self.app.smart_homes[0].name)  # first item in array should be first house name
        else:
            self.home_name.set("")#don't actually think I need this but whatever

        self.home_selection()

    def run(self):
        self.window.mainloop()

    def home_selection(self):
        for widget in self.main_frame.winfo_children():  # this works don't question in
            widget.destroy()  # watch the indentation

        if self.app.smart_homes:
            self.home_name.set(self.app.smart_homes[0].name)

        task_label_2 = Label(
            self.main_frame,
            text="Select a home",
        )
        task_label_2.grid(row=0, column=2)

        home_dropdown = OptionMenu(
            self.main_frame,
            self.home_name,
            *[home.name for home in self.app.smart_homes]
        )
        home_dropdown.grid(row=1, column=2,  padx=(0, 120), pady=(0,30))
        home_dropdown.configure(width=10)#make it wider

        task_label = Label(
            self.main_frame,
            text="Input Home name"
        )
        task_label.grid(row=2, column=2)

        new_home_entry = Entry(self.main_frame, width=20)
        new_home_entry.grid(row=3, column=2, padx=(0,120), pady=(0,30))
        new_home_entry.configure(width=15)#make it wider and look less weird

        select_button = Button(  # select house
            self.main_frame,
            text="Select Home",
            command=self.select_home,
            width=12,
        )
        select_button.grid(row=1, column=2, padx=(120,0), pady=(0,30))

        add_home_button = Button(  # select house
            self.main_frame,
            text="Add new Home",
            command=lambda: self.add_home(new_home_entry.get()),
            width=12,
        )
        add_home_button.grid(row=3, column=2, padx=(120, 0), pady=(0,30))

        task_label_3 = Label(
            self.main_frame,
            text="Additional features"
        )
        task_label_3.grid(row=4, column=2)

        save_button = Button(  # select house
            self.main_frame,
            text="Save Homes",
            command=self.app.save_devices,
            width=12,
        )
        save_button.grid(row=5, column=2, padx=(120,0), pady=5)

        remove_home_button = Button(  # select house
            self.main_frame,
            text="Remove Home",
            command=self.remove_home,
            width=12,
        )
        remove_home_button.grid(row=5, column=2, padx=(0,120), pady=5)

        home_remove_error = Label(
            self.main_frame,
            textvariable = self.home_delete_error,
            fg="red"
        )
        home_remove_error.grid(row=6, column=2, padx=0)

    def add_home(self, name):
        if name:
            self.app.add_home(name)
        self.home_selection()

    def remove_home(self):
        home_name = self.home_name.get()
        if home_name:
            if len(self.app.smart_homes) > 1:
                self.app.remove_home(home_name)
            else:
                self.home_delete_error.set("Cannot delete all homes you'll be homeless")
        self.home_selection()

    def select_home(self):
        home_name = self.home_name.get()
        selected_home = self.app.get_home(home_name)
        if selected_home:
            self.home_delete_error.set("")
            self.create_widget(selected_home)
        else:
            print("Home isn't there")

    def create_widget(self, home: SmartHome):
        for widget in self.main_frame.winfo_children():# this works don't question in
            widget.destroy() # watch the indentation

        add_button = Button(
            self.main_frame,
            text="Add Device",
            command=lambda : self.handle_add_devices(home),
            width=9,
            relief="raised",
            borderwidth=3
        )
        add_button.grid(row=len(home.devices) + 2, column=0, padx=20, pady=10, sticky="w")

        button_num_1 = Button(
            self.main_frame,
            text="Turn On All",
            command=lambda: self.handle_switch_all_on(home),
            width=20,
            bg="lightblue",
            relief="raised",
            borderwidth=3
        )
        button_num_1.grid(row=0, column=0, padx=10, pady=5)

        button_num_2 = Button(
            self.main_frame,
            text="Turn Off All",
            command=lambda: self.handle_switch_all_off(home),
            bg="lightblue",
            width=21,
            relief="raised",
            borderwidth=3
        )
        button_num_2.grid(row=0, column=1, padx=(0, 35), pady=5)

        for index, item in enumerate(home.devices, start=1):
            device_type = type(item).__name__.lower()
            measurement = " "

            if isinstance(item, SmartFridge)and device_type == "smartfridge":
                device_type = "Fridge"
                measurement = "Temperature: " + str(item.temp)
            elif isinstance(item, SmartLight) and device_type == "smartlight":
                device_type = "Light"
                measurement = "Brightness: " + str(item.brightness)
            elif isinstance(item, SmartPlug) and device_type == "smartplug":
                device_type = "Plug"
                measurement = "Consumption: " + str(item.consumption_rate)

            state = "On" if item.switched_on else "Off"

            label = Label(
                self.main_frame,
                text=f"{device_type.capitalize()}: {state},  {measurement}",
                width=30,
                highlightbackground="black",
                highlightthickness=3
            )
            label.grid(row=index, column=0, padx=20, pady=5)

            toggle_button = Button(
                self.main_frame,
                text="Toggle",
                command=lambda i=index - 1: self.handle_device_toggle(i, home),
                width=9,
                relief="raised",
                borderwidth=3
            )
            toggle_button.grid(row=index, column=1, padx=(0, 110), pady=5)

            edit_button = Button(
                self.main_frame,
                text="Edit",
                command=lambda i=index - 1: self.handle_edit(i, home),
                width=9,
                relief="raised",
                borderwidth=3
            )
            edit_button.grid(row=index, column=1, padx=(60, 0), pady=5)

            delete_button = Button(
                self.main_frame,
                text="Delete",
                command=lambda i=index - 1: self.handle_delete(i, home),
                width=9,
                relief="raised",
                borderwidth=3
            )
            delete_button.grid(row=index, column=2, padx=(0, 10), pady=5)

            back_button = Button(
                self.main_frame,
                text= "Back to main",
                command=self.home_selection,
                width=20,
                relief="raised",
            )
            back_button.grid(row=len(home.devices) + 3, column=0, padx=20, pady=10, sticky="w")

    def handle_switch_all_on(self, home):
        home.switch_all_on()
        self.create_widget(home)

    def handle_switch_all_off(self, home):
        home.switch_all_off()
        self.create_widget(home)

    def handle_device_toggle(self, index ,home):
        home.toggle_device(index)
        self.create_widget(home)

    def handle_edit(self, index, home):
        Editor(index, home.devices, self.create_widget, home)

    def handle_delete(self, index, home):
        if 0 <= index < len(home.devices):
            home.devices.pop(index)
            self.create_widget(home)

    def handle_add_devices(self, home):
        AddWidget(self.window, home.devices, home, self.create_widget)

def test_smart_home_system():
    app = SmartHomeApp()

    if not app.smart_homes:
        app.add_home("Default")

    gui = SmartHomeGUI(app)
    gui.run()

test_smart_home_system()