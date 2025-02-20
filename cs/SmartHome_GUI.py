from tkinter import Tk, Frame, Label, Button
from SmartLight import SmartLight
from smartFridge import SmartFridge
from smartPlug import SmartPlug
from smartHome import SmartHome
from EditWidget import Editor
from AddWidget import AddWidget

class SmartHomeGUI:

    def __init__(self):
        super().__init__()
        self.window = Tk()
        self.window.title("Smart Home GUI")
        self.window.geometry("700x500")
        self.window.configure(bg="lightblue", borderwidth=3, highlightbackground="black") # use configure to alter the background elements
        self.main_frame = Frame(self.window)
        self.main_frame.pack(padx=10, pady=10)

        self.smart_home = SmartHome()
        self.editor = Editor


    def run(self):
        self.create_widget()
        self.window.mainloop()

    def create_widget(self):

        for widget in self.main_frame.winfo_children():# this works dont question in
            widget.destroy() # watch the indentation or shit breaks

        add_button = Button(
            self.main_frame,
            text="Add Device",
            command=self.handle_add_devices,
            width=9,
            relief="raised",
            borderwidth=3
        )
        add_button.grid(row=len(self.smart_home.devices) + 2, column=0, padx=20, pady=10, sticky="w")

        button_num_1 = Button(
            self.main_frame,
            text="Turn On All",
            command=self.handle_switch_all_on,
            width=20,
            bg="lightblue",
            relief="raised",
            borderwidth=3
        )
        button_num_1.grid(row=0, column=0, padx=10, pady=5)

        button_num_2 = Button(
            self.main_frame,
            text="Turn Off All",
            command=self.handle_switch_all_off,
            bg="lightblue",
            width=21,
            relief="raised",
            borderwidth=3
        )
        button_num_2.grid(row=0, column=1, padx=(0, 35), pady=5)

        for index, item in enumerate(self.smart_home.devices, start=1):
            device_type = type(item).__name__.lower()
            measurement = "" # <---- this is also a cunt

            if isinstance(item, SmartFridge)and device_type == "Fridge":
                device_type = "Fridge"
                measurement = "Temperature: " + str(item.temp)
            elif isinstance(item, SmartLight) and device_type == "Light":
                device_type = "Light"
                measurement = "Brightness: " + str(item.brightness)
            elif isinstance(item, SmartPlug) and device_type == "Plug":
                device_type = "Plug"
                measurement = "Consumption: " + str(item.consumption_rate)

            state = item.switched_on

            label = Label(
                self.main_frame,
                text=str(device_type.capitalize()) + ": " + str(state) + ", " + str(measurement),
                width=30,
                highlightbackground="black",
                highlightthickness=3
            )
            label.grid(row=index, column=0, padx=20, pady=5)

            toggle_button = Button(
                self.main_frame,
                text="Toggle",
                command=lambda i=index - 1: self.handle_device_toggle(i),
                width=9,
                relief="raised",
                borderwidth=3
            )
            toggle_button.grid(row=index, column=1, padx=(0, 110), pady=5)

            edit_button = Button(
                self.main_frame,
                text="Edit",
                command=lambda i=index - 1: self.handle_edit(i),
                width=9,
                relief="raised",
                borderwidth=3
            )
            edit_button.grid(row=index, column=1, padx=(60, 0), pady=5)

            delete_button = Button(
                self.main_frame,
                text="Delete",
                command=lambda i=index - 1: self.handle_delete(i),
                width=9,
                relief="raised",
                borderwidth=3
            )
            delete_button.grid(row=index, column=2, padx=(0, 10), pady=5)

    #another note to self stop being fucking stupid
    #details help i made a whole new file jsut to refresh these adn a ton of stuff broke
    def handle_switch_all_on(self):
        self.smart_home.switch_all_on()
        self.create_widget()

    def handle_switch_all_off(self):
        self.smart_home.switch_all_off()
        self.create_widget()

    def handle_device_toggle(self, index):
        self.smart_home.toggle_device(index)
        self.create_widget()

    def handle_edit(self, index):
        Editor(self.window, index, self.smart_home.devices, self.create_widget)

    def handle_delete(self, index):
        if 0 <= index < len(self.smart_home.devices):
            self.smart_home.devices.pop(index)
            self.create_widget()

    def handle_add_devices(self):
        AddWidget(self.window, self.smart_home.devices, self.smart_home, self.create_widget)

    def __str__(self):
        devices = [str(device) for device in self.smart_home.devices]
        return "\n".join(devices)

def main():
    home = SmartHomeGUI()

    # Create some devices
    fridge = SmartFridge(3)
    light = SmartLight(28)
    plug = SmartPlug(79)

    home.smart_home.add_devices(fridge)
    home.smart_home.add_devices(light)
    home.smart_home.add_devices(plug)

    print(home)

    home.run()
main()