from tkinter import Tk, Frame, Label, Button
import csv
from SmartLight import SmartLight
from smartPlug import SmartPlug
from smartFridge import SmartFridge
from smartHome import SmartHome


class SmartHomeApp:

    def __init__(self, csv_file = "smart_homes.csv"):
        self.csv_file = csv_file
        self.smart_homes = []
        self.load_devices()

    def load_devices(self):#load the stuff into the array
        try:
            with open(self.csv_file, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    home_name = row[0]
                    device_type = row[1]
                    device_state = row[2]
                    device_info = row[3]

                    home = next((home for home in self.smart_homes if home.name == home_name),None)
                    if not home:
                        home = SmartHome(home_name)
                        self.smart_homes.append(home)

                    if device_type ==  "SmartLight":
                        light = SmartLight(int(device_info))#measurement import
                        light.switched_on = device_state == "On"
                        home.add_devices(light)
                    elif device_type ==  "SmartFridge":
                        fridge = SmartFridge(int(device_info))#measurement import
                        fridge.switched_on = device_state == "On"
                        home.add_devices(fridge)
                    elif device_type ==  "SmartPlug":
                        plug = SmartPlug(int(device_info))#measurement import
                        plug.switched_on = device_state == "On"
                        home.add_devices(plug)


        except FileNotFoundError:
                print("Your file could not be found where you have specified check it again")

    def save_devices(self):
        with open(self.csv_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            for home in self.smart_homes:
                for device in home.devices:
                    device_type = type(device).__name__
                    state = "On" if device.switched_on else "Off"
                    if isinstance(device, SmartFridge):
                        device_info = device.temp
                    elif isinstance(device, SmartLight):
                        device_info = device.brightness
                    elif isinstance(device, SmartPlug):
                        device_info = device.consumption_rate
                    writer.writerow([home.name, device_type, state, device_info])

    def add_home(self, name):
        home = SmartHome(name)
        self.smart_homes.append(home)

    def remove_home(self, name):
        self.smart_homes = [home for home in self.smart_homes if home.name != name]

    def list_homes(self):
        return [home.name for home in self.smart_homes]

    def get_home(self, name):
        return  next((home for home in self.smart_homes if home.name == name), None)

    def __str__(self):
        result = []
        for home in self.smart_homes:
            result.append(f"Smart Home: {home.name}")
            for index, device in enumerate(home.devices):
                result.append(f"{index + 1}. {device}: State: {'On' if device.switched_on else 'Off'}")
            return "\n".join(result)


