from graphix import *

def get_name():
    while True:
        name = str(input("What is your first name: ")).strip()

        if name.isalpha():
            print(f"Your name is {name}")
            break
        else:
            print("the name you have input is invalid")


def traffic_lights():
    import time

    win = Window("Traffic Lights", 200, 300)

    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)

    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)

    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)

    while True:
        red.fill_colour = "red"
        amber.fill_colour = "black"
        green.fill_colour = "black"
        time.sleep(2)

        red.fill_colour = "red"
        amber.fill_colour = "yellow"
        green.fill_colour = "black"
        time.sleep(1)

        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        time.sleep(2)

        red.fill_colour = "black"
        amber.fill_colour = "yellow"
        green.fill_colour = "black"
        time.sleep(1)


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

def order_price():
    sum_total = 0

    while True:

        price = float(input("What is the unit price of this item: "))
        quantity = int(input("How many of this item do you need: "))

        if isinstance(price, float) and int(quantity) > 0:
            total = price * quantity
            sum_total += total

            choice = input("Are there any more items y/n: ").upper()
            if choice == "Y":
                continue
            else:
                print("Exiting order list")
                break
        else:
            "Your values were not accepted"

    print(f"The total of your order items is {sum_total}")


def draw_circle(x, y, radius, color, window):
    circle = Circle(Point(x, y), radius)
    circle.fill_colour = color
    circle.draw(window)


def clickable_eye(x, y):
    window = Window("Eyes", 500, 500)

    # Draw the eye
    draw_circle(x, y, 120, "white", window)
    draw_circle(x, y, 60, "light blue", window)
    draw_circle(x, y, 30, "black", window)

    message = None

    while True:
        click = window.get_mouse()

        distance = ((click.x - x) ** 2 + (click.y - y) ** 2) ** 0.5

        if distance <= 30:
            new_message = "You clicked on the pupil"
        elif distance <= 60:
            new_message = "You clicked on the iris"
        elif distance <= 120:
            new_message = "You clicked on the sclera"
        else:
            new_message = "Click detected outside the eye. Exiting..."
            if message: # checking if the message already exists
                message.undraw()
            message = Text(Point(250, 400), new_message)
            message.draw(window)
            time.sleep(1)
            window.close()
            break

        if message: # if it does not creates a new message
            message.undraw()
        message = Text(Point(250, 400), new_message)
        message.draw(window)

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def temperature_converter():

    while True:
        print("1: fahrenheit  - celsius")
        print("2: celsius - fahrenheit")
        choice = int(input("Make your choice from the options above: "))

        if choice == 1:
            number = float(input("What fahrenheit temp are you converting to celsius: "))
            result = fahrenheit_to_celsius(number)
            print(f"{number}°F is equal to {result:.2f}°C")
        elif choice == 2:
            number = float(input("What celsius temp are you converting to fahrenheit: "))
            result = celsius_to_fahrenheit(number)
            print(f"{number}°C is equal to {result:.2f}°F")
        else:
            print("Your choice was not accepted, try again.")

        selection = str(input("Do you want to run this again (y/n): ")).upper()

        if selection == "Y":
            continue
        else:
            print("Exiting program.")
            break

def table_tennis_scorer():

    window = Window("Table Tennis", 500, 500)

    score_1 = 0
    score_2 = 0
    line = Line(Point(250,0),Point(250, 500))
    line.outline_colour = "black"
    line.draw(window)

    score_1_text = Text(Point(125, 250), '0')
    score_2_text = Text(Point(375, 250), '0')

    score_1_text.draw(window)
    score_2_text.draw(window)

    winner_1 = Text(Point(125, 300), " ")
    winner_2 = Text(Point(375, 300), " ")

    winner_1.draw(window)
    winner_2.draw(window)

    while True:

        score = window.get_mouse()

        if score.x <= 250:
            score_1 += 1
            score_1_text.text = str(score_1)
        else:
            score_2 += 1
            score_2_text.text = str(score_2)

        if score_1 == 11:
            winner_1.text = "Player 1 Wins"
            break
        elif score_2 == 11:
            winner_2.text = "Player 2 Wins "
            break


    window.get_mouse()
    window.close()

table_tennis_scorer()
