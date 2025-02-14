# pract 10
class Square:
    def __init__(self, square_length, square_width):
        self.outline_color = "black"
        self.fill_color = "white"
        self.length = square_length
        self.width = square_width

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4

    def get_center(self):
        center_len = self.length / 2
        center_width = self.width / 2
        return f"Center of your square is MyPoint({center_len}, {center_width})"

    def __str__(self):
        return f"Square outline color is {self.outline_color} and fill color is {self.fill_color}"


class MyCircle:
    def __init__(self, center_x, center_y, outline_color, fill_color, radius):
        self.center_x, self.center_y = center_x, center_y
        self.outline_color = outline_color
        self.fill_color = fill_color
        self.radius = radius

    def get_center(self):
        pass

    def __str__(self):
        return f"the center of the circle is {self.center_x, self.center_y}, the radius is {self.radius}, the outline color is {self.outline_color}, and the fill color is {self.fill_color}"


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.name = "Alicia Keys"

    def __str__(self):
        return f"Current account balance is {self.balance}"

    def balance_check(self, withdraw_ammount):
        if self.balance - withdraw_ammount <= 0:
            self.balance = self.balance
        else:
            self.balance -= withdraw_ammount


class HotelRoom:
    def __init__(self):
        self.room_number = 0
        self.occupant_name = "john smith"

    def is_occupied(self):
        room_booked = [101, 105, 107, 109]
        guest_booked = ["John Silver", "Keri Altman", "Gordon Lunt", "Mitch Mconnel"]

        if self.room_number in room_booked:
            return "Room is Booked already"
        elif self.occupant_name in guest_booked:
            return "This guest is already booked in"
        else:
            return f"The room {self.room_number} is available for {self.occupant_name}"


class GradeBook:
    def __init__(self):
        self.grades = {}

    def add_grades(self, module_name, grade):
        if isinstance (grade, int) and grade >= 0:
            self.grades[module_name] = grade
        else:
            print("Whatever the hell you input isn't allowed")

    def average_grades(self):
        if len(self.grades) == 0:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)

    def __str__(self):
        if not self.grades:
            return "Gradebook is empty"
        return "\n".join(f"{module}: {grade}" for module, grade in self.grades.items())


def test_square():
    square = Square(5, 0)

    print(f"Default outline is {square.outline_color} and fill color is {square.fill_color}")

    square.outline_color = "red"
    square.fill_color = "orange"

    print(f"Changing square outline to {square.outline_color} and the fill color to {square.fill_color}")

    print(square)


# test_square()


def test_square_2():
    square = Square(5, 0)

    print(f"length of a side is {square.length}")
    print(f"area is {square.area()}")
    print(f"perimeter is {square.perimeter()}")


# test_square_2()


def test_square_3():
    square = Square(10, 7)
    print(f"{square.get_center()}")


# test_square_3()


def test_circle_1():
    circle = MyCircle(1, 5, "Green", "Blue", 6)

    print(circle)


# test_circle_1()


def bank_account_1():
    account = BankAccount()

    print(f"Account holders name is {account.name}")
    print(account)

    account.balance = 100

    print(f"Depositing £{account.balance}")
    print(account)

    account.balance = 50

    print(f"withdrawing £{account.balance}")
    print(account)

    account.balance_check(100)

    print("Withdrawing £100")
    print(account)
#bank_account_1()

def hotel_room_1():
    hotel = HotelRoom()

    hotel.occupant_name = "John Williams"
    hotel.room_number = 102

    print(hotel.is_occupied())
#hotel_room_1()

def gradebook_1():
    gradebook = GradeBook()

    gradebook.add_grades("Math", 88)
    gradebook.add_grades("Physics", 68)
    gradebook.add_grades("History", 78)

    print(gradebook)
    print("The average grade is: ", gradebook.average_grades())
gradebook_1()


