from operator import index

from SmartLight import SmartLight
from smartFridge import SmartFridge
from smartPlug import SmartPlug

class SmartHome:

    def __init__(self):
        self.devices = []

    def add_devices(self, device):
        self.devices.append(device)

    def get_device(self, index):
        return self.devices[index]

    def toggle_device(self, index):
        device = self.devices[index]
        device.toggle_switch()

    def switch_all_on(self):
        for device in self.devices:
            if not device.switched_on:
                device.toggle_switch()

    def switch_all_off(self):
        for device in self.devices:
            if device.switched_on:
                device.toggle_switch()

    def __str__(self):
        devices = [f"{index + 1}. {str(device)}" for index, device in enumerate(self.devices)]
        return "\n".join(devices)


def test_smart_home():
    home = SmartHome()

    # Create some devices
    fridge = SmartFridge(3)
    light = SmartLight(28)
    plug = SmartPlug(79)

    home.add_devices(fridge)
    home.add_devices(light)
    home.add_devices(plug)

    #home.switch_all_on()
    #print(home)

    home.toggle_device(2)
    print(home)

test_smart_home()


