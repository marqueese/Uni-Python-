from graphix import *

def fast_food_order_price():
    price = float(input("How much is the order: :"))
    delivery = 0

    if price < 20:
        delivery = 2.50

    price_total = price + delivery

    print(f"Your order total is {price_total}")

def what_to_do_today():
    temp = float(input("What's the temperature in °C: "))

    if temp > 50:
        print("You're dead just accept it")
    elif temp > 25:
        print("Go for a swim in the sea")
    elif 10 <= temp <= 25:
        print("Go shopping in Gunwharf Quays")
    elif temp < 10:
        print("Stay indoors and watch a film")


def display_square_routes(start, end):
    for i in range(start, end):
        print(f"The square Roue of {i} is {i ** 0.5}")

#display_square_routes(4, 7)

def calculate_grade(mark):
    if mark > 20 or mark < 0:
        print("Invalid mark must be between 0 & 20")
    elif  mark >= 16:
        print("Your grade is an A")
    elif mark >=12:
        print("Your grade is a B")
    elif mark >=8:
        print("Your grade is a C")
    elif mark < 8:
        print("You're a failure")
    else:
        print("Your mark was not accepted try again")

#calculate_grade(16)

def peas_in_a_pod():
    peas = int(input("How many peas are in this pod: "))

    window = Window("Peas in a Pod", peas * 100, 100)
    i = 50

    for _ in range(peas):
        pea = Circle(Point(i, 50), 50)
        pea.fill_colour = "green"
        pea.draw(window)
        i += 100

    window.get_mouse()
    window.close()

def ticket_price(distance, age):

    ticket = 10.00
    per_km = 0.15

    mileage_cost = distance * per_km
    total_cost = mileage_cost + ticket

    if age > 60 or age < 15:
        reduced_cost  = total_cost * 0.6
        print(reduced_cost)
    else:
        print(total_cost)

#ticket_price(20, 12)

def numbered_square(n):
    for row in range(n, 0, -1):
        row_numbers = []
        for col in range(row, row + n):
            row_numbers.append(col)
        print(" ".join(map(str, row_numbers)))
#numbered_square(5)

def eye_picker():
    window = Window("Eye Picker", 400, 400)

    while True:
        print("It is a 400x400 window.")
        x_cord = int(input("Where is the x coordinate of your eye? (between 30 and 370): "))
        y_cord = int(input("Where is the y coordinate of your eye? (between 30 and 370): "))

        print("\nWhat will the color of the eye be?")
        print("Blue\nGrey\nGreen\nBrown")
        color = str(input("Write one color: ")).lower()

        if 30 <= x_cord <= 370 and 30 <= y_cord <= 370:
            circle = Circle(Point(x_cord, y_cord), 30)
            circle.fill_colour = color
            circle.draw(window)
            print(f"Eye placed at ({x_cord}, {y_cord})")
            break
        else:
            print("Coordinates are out of range. The center of the circle must be at least 30 pixels from each border.")

    window.get_mouse()
    window.close()


def display():
    window = Window("Shapes", 500, 500)

    for i in range(0, 500, 100):
        line1 = Line(Point(0, i), Point(i, 0))
        line1.draw(window)
        line1.fill_colour = "blue"

        line2 = Line(Point(i, 500), Point(500, i))
        line2.draw(window)
        line2.fill_colour = "red"


    for i in range(0, 500, 100):
        line3 = Line(Point(0, 500 - i), Point(i, 500))
        line3.draw(window)
        line3.fill_colour = "blue"

        line4 = Line(Point(i, 0), Point(500, 500 - i))
        line4.draw(window)
        line4.fill_colour = "red"


    window.get_mouse()
    window.close()


display()

