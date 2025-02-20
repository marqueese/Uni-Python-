from smartPlug import SmartPlug

class SmartLight(SmartPlug):

    def __init__(self, consumption_rate, brightness=50):
        super().__init__(consumption_rate)
        self.switched_on = False
        if 0 <= brightness <= 100:
            self._percentage = brightness
        else:
            self._percentage = None
            print("Item was not created due to invalid brightness")

    @property
    def brightness(self):
        return self._percentage

    @brightness.setter
    def brightness(self, brightness):
        if 0 <= brightness <= 100:
            self._percentage = brightness
        else:
            print("Invalid Brightness selected, must be between 0-100")


    def __str__(self):#
        if self._percentage is None:
            return "SmartLight was not created due to invalid brightness"
        else:
            state = "on" if self.switched_on else "off"
            return f"SmartLight is {state} with a brightness of {self.brightness}"

"""
def test_smart_light():
    light = SmartLight(80)
    print(light)

    light.brightness = -3

    light.toggle_switch()
    print(light)

test_smart_light()
"""