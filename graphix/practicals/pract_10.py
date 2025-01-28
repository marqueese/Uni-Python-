from scipy.signal import square


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



def test_square():
    square = Square(5, 0)

    print(f"Default outline is {square.outline_color} and fill color is {square.fill_color}")

    square.outline_color = "red"
    square.fill_color = "orange"

    print(f"Changing square outline to {square.outline_color} and the fill color to {square.fill_color}")

    print(square)

#test_square()

def test_square_2():
    square = Square(5, 0)

    print(f"length of a side is {square.length}")
    print(f"area is {square.area()}")
    print(f"perimeter is {square.perimeter()}")

#test_square_2()

def test_square_3():
    square = Square(10, 7)
    print(f"{square.get_center()}")

test_square_3()

