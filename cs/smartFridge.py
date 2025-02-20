from smartPlug import SmartPlug

class SmartFridge(SmartPlug):

    def __init__(self, temp=3):
        self.switched_on = False
        if temp == 1 or temp == 3 or temp == 5:
            self._temperature = temp
        else:
            self._temperature = None
            print("Item was not created due to invalid temperature selection")

    @property
    def temp(self):
        return self._temperature

    @temp.setter
    def temp(self, temp):
        if temp == 1 or temp == 3 or temp == 5:
            self._temperature = temp
        else:
            print("Invalid Temperature selected, must be between either 1, 3, or 5")


    def __str__(self):
        if self._temperature is None:
            return "SmartFridge was not created due to invalid Temperature selection"
        else:
            state = "on" if self.switched_on else "off"
            return f"SmartFridge is {state} with a temperature of of {self.temp}"

"""
def test_smart_fridge():
    fridge = SmartFridge(3)
    print(fridge)

    fridge.temp = -3 #invalid reverts to previous
    print(fridge)

test_smart_fridge()
"""