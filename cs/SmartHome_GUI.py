from tkinter import Tk, Frame, Button
from SmartHome import SmartHome
from SmartLight import SmartLight
from smartFridge import SmartFridge
from smartPlug import SmartPlug


class SmartHomeGUI(SmartHome):
    def __init__(self):
        super().__init__()
        self.window = Tk()
        self.window.title("Smart Home GUI")
        self.window.geometry("900x400")
        self.window.configure(bg="lightblue")  # Background color

        self.main_frame = Frame(self.window)
        self.main_frame.pack(padx=10, pady=10)

    def run(self):
        self.create_widget()  # Build the initial GUI
        self.window.mainloop()

    def create_widget(self):
        # Buttons for turning devices on/off
        button_turn_on = Button(
            self.main_frame,
            text="Turn On All",
            command=self.handle_switch_all_on,  # Updated to use the new handler
            width=40,
            relief="ridge",
            bg="lightblue"
        )
        button_turn_on.grid(row=0, column=0, padx=20, pady=5)

        button_turn_off = Button(
            self.main_frame,
            text="Turn Off All",
            command=self.handle_switch_all_off,  # Updated to use the new handler
            width=40,
            relief="ridge",
            bg="lightblue"
        )
        button_turn_off.grid(row=0, column=1, padx=20, pady=5)

        # Refresh device widgets
        for index, item in enumerate(self.devices, start=1):
            device_type = type(item).__name__.lower()
            state = "On" if item.switched_on else "Off"
            measurement = ""

            if isinstance(item, SmartFridge):
                measurement = f"Temperature: {item.temp}"
            elif isinstance(item, SmartLight):
                measurement = f"Brightness: {item.brightness}"
            elif isinstance(item, SmartPlug):
                measurement = f"Consumption: {item.consumption_rate}"

            label = Label(
                self.main_frame,
                text=f"{device_type.capitalize()}: {state}, {measurement}",
                width=30
            )
            label.grid(row=index, column=0, padx=0, pady=5)

    def handle_switch_all_on(self):
        """
        Handles the "Turn On All" button click.
        """
        self.switch_all_on()  # Call the SmartHome method to turn everything on
        self.create_widget()  # Refresh the GUI to show the updated state

    def handle_switch_all_off(self):
        self.switch_all_off()  # Call the SmartHome method to turn everything off
        self.create_widget()  # Refresh the GUI to show the updated state





def main():
    home = SmartHomeGUI()

    # Create some devices
    fridge = SmartFridge(3)
    light = SmartLight(28)
    plug = SmartPlug(79)

    home.add_devices(fridge)
    home.add_devices(light)
    home.add_devices(plug)

    print(home.devices)  # Print the device list for debugging
    home.run()


main()
