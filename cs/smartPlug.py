class SmartPlug:

    def __init__(self, consumption_rate):
        self.switched_on = False
        self.error_message = ""
        if 0 <= consumption_rate <= 150:
            self._consumption_rate = consumption_rate
        else:
            self._consumption_rate = None
            self.error_message = "Item was not created"

    def toggle_switch(self):
        self.switched_on = not self.switched_on

    @property
    def consumption_rate(self):
        return self._consumption_rate

    @consumption_rate.setter
    def consumption_rate(self, value):
        if 0 <= value <= 150:
            self._consumption_rate = value
        else:
            self.error_message = "Invalid consumption rate, must be between 0-150"

    def __str__(self):
        if self._consumption_rate is None:
            return "Smart plug was not created due to invalid consumption rate"
        else:
            state = "on" if self.switched_on else "off"
            return f"SmartPlug is {state} with a consumption rate of {self.consumption_rate}"

'''
def test_smart_plug():
    plug_1 = SmartPlug(45)
    print(plug_1)

    plug_1.toggle_switch()
    print(plug_1)

    plug_1.consumption_rate = 98
    print(plug_1)

    plug_1.consumption_rate = -70
    print(plug_1)

    plug_1.toggle_switch()
    print(plug_1)

    plug_2 = SmartPlug(-90)
    print(plug_2)
test_smart_plug()
'''