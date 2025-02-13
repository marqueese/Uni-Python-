class CallCenter:

    def __init__(self):
        self.workstations = []
        self.current_state = "False"

    def add_workstations(self, workstation):
        self.workstations.append(workstation)

    def toggle_power(self):
        if self.current_state == "False":
            self.current_state = "True"
        elif self.current_state == "True":
            self.current_state = "False"
        else:
            self.current_state = "False"

    def device_count(self):
        return len(self.workstations)

    def get_workstation(self, index):
        return self.workstations[index]


class WorkStation:
    def __init__(self):
        self.turned_on = False


def main():
    call_center = CallCenter()

    ws1 = WorkStation()
    ws1.turned_on = True
    ws2 = WorkStation()
    ws3 = WorkStation()

    call_center.add_workstations(ws1)
    call_center.add_workstations(ws2)
    call_center.add_workstations(ws3)

    print(call_center.get_workstation(0).turned_on)

main()