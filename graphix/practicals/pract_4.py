from graphix import *
import os
os.chdir("Text_Files")
os.getcwd()
os.listdir()


def personal_greeting():
        name = input("What is your name: ")
        print("Well hello there,", name, "How are you today?")

def formal_name():
        fname = input("What is your forename: ")
        sname = input("What is your surname: ")

        f_letter = fname[0]

        print(f_letter.upper(),".",sname)

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    ounces = round(ounces, 2)
    print("The weight of",kilos,"kilos in ounces is:",ounces)

def generate_email():
        fname = input("What is your forename: ")
        sname = input("What is your surname: ")
        year = input("When will be your first year in university: ")

        fname = fname[0]
        sname = sname[0:4]
        year = year[2:4]

        print("Your uni email is")
        print(f"{sname}.{fname}.{year}@myport.ac.uk")

def grade_test():
        grades = "FFFCCBBAAA"

        mark = int(input("Enter your mark (0-10): "))
        grade = grades[max(0, min(10, mark))]
        print(f"Your grade is: {grade}")

def graphic_letters():
        window = Window("The Graph of stuff", 500, 500)

        word = input("Enter a word: ")
        variable = 0

        for ch in word:

                letter = word[variable]

                click = window.get_mouse()
                Letter_Display = Text(click, letter)
                Letter_Display.draw(window)

                variable += 1
        window.close()

def sing_a_song():
        word = input("Enter a word: ")
        wps = int(input("how many times a line: "))
        rows = int(input("how many rows of this: "))

        for words in range (rows):
                print(f"{word * wps}")

def conversion_table():
    exchange_rate = 1.17

    print(f"{'Euros':>10} {'Pounds':>10}")
    print("-" * 22)

    for euros in range(21):
        pounds = euros / exchange_rate
        print(f"{euros:>10} {pounds:>10.2f}")

def make_initialism():
    phrase = input("enter your stuff: ")

    words = phrase.split()

    initialism = "".join(word[0].upper() for word in words)

    print(initialism)

def file_in_caps():
    input_file = open("Quotations.txt", "r")

    contents = input_file.read()
    print(contents.upper())
    input_file.close()

def total_spending():
    value = 0

    with open("Spending.txt", "r") as input_file:
        for line in input_file:
            value += float(line)
    print(f"Total spending: {value}")

def name_to_number():
    name = input("Enter your name: ").lower()

    total_value = 0

    for char in name:
        if char.isalpha():
            letter_value = ord(char) - ord('a') + 1
            total_value += letter_value

    print(f"The numerical value of your name is: {total_value}")

def rainfall_chart ():
    with open("rainfall.txt", "r") as input_file:
        lines = input_file.readlines()

        locations_array = []
        rainfall_array = []

        for line in lines:
            parts = line.rsplit(" ", 1)  # Split by the last space
            location = parts[0]
            rainfall = int(parts[1])

            locations_array.append(location)
            rainfall_array.append(rainfall)

    for location, rainfall in zip(locations_array, rainfall_array):
        print(f"{location} {rainfall} {'*' * rainfall}")

def rainfall_graphics():
    window = Window("Rainfall Graph", 500, 500)

    # Open the rainfall data file
    with open("rainfall.txt", "r") as input_file:
        lines = input_file.readlines()

        locations_array = []
        rainfall_array = []

        for line in lines:
            parts = line.rsplit(" ", 1)  # Split by the last space
            location = parts[0]
            rainfall = int(parts[1])

            locations_array.append(location)
            rainfall_array.append(rainfall)

        # Draw each location and its rainfall based on user clicks
        for location, rainfall in zip(locations_array, rainfall_array):
            click_point = window.get_mouse()  # Wait for user to click the position

            # Draw the location name
            location_text = Text(click_point, location)
            location_text.draw(window)

            # Draw the rainfall as asterisks just below the location text
            rainfall_text_point = Point(click_point.get_x(), click_point.get_y() + 20)
            rainfall_message = "*" * rainfall
            rain = Text(rainfall_text_point, rainfall_message)
            rain.draw(window)

    # Wait for final click to close the window
    window.get_mouse()
    window.close()


def five_click_stick_figure():
    window = Window("Stick Figure", 400, 400)

    # Click 1: Top center of the head
    p1 = window.get_mouse()

    # Click 2: Radius of the head
    p2 = window.get_mouse()
    radius = ((p2.get_x() - p1.get_x()) ** 2 + (p2.get_y() - p1.get_y()) ** 2) ** 0.5
    head = Circle(p1, radius)
    head.draw(window)

    # Click 3: Body start (only y-coordinate changes)
    p3 = window.get_mouse()
    body_start = Point(p1.get_x(), p3.get_y())
    body = Line(p1, body_start)
    body.draw(window)

    # Click 4: Left foot position
    left_foot = window.get_mouse()
    left_leg = Line(body_start, left_foot)
    left_leg.draw(window)

    # Click 5: Right foot position
    right_foot = window.get_mouse()
    right_leg = Line(body_start, right_foot)
    right_leg.draw(window)

    # Draw the arms at a midpoint between head and body start
    arm_y = (p1.get_y() + p3.get_y()) / 2
    left_hand = Point(p1.get_x() - radius, arm_y)
    right_hand = Point(p1.get_x() + radius, arm_y)
    left_arm = Line(left_hand, Point(p1.get_x(), arm_y))
    right_arm = Line(right_hand, Point(p1.get_x(), arm_y))
    left_arm.draw(window)
    right_arm.draw(window)

    # To use five_click_stick_figure
    window.get_mouse()  # Keep the window open
    window.close()


def menu():
    while True:
        print("\nPlease select an option:")
        print("1. Personal Greeting")
        print("2. Formal name")
        print("3. Kilos to ounces")
        print("4. Generate email")
        print("5. Grade test")
        print("6. Letter thingy")
        print("7. Sing a song ")
        print("8. Conversion Table ")
        print("9: Make Initialism")
        print("10: File in Caps")
        print("11: Total Spending")
        print("12: Name to number")
        print("13: Rainfall chart")
        print("14: Rainfall graphics")
        print("15: stick figures")
        print("0. Exit")

        choice = input("\nEnter the number of your choice: ")

        if choice == '1':
            personal_greeting()
        elif choice == '2':
            formal_name()
        elif choice == '3':
            kilos_to_ounces()
        elif choice == "4":
                generate_email()
        elif choice == "5":
                grade_test()
        elif choice == "6":
                graphic_letters()
        elif choice == "7":
                sing_a_song()
        elif choice == "8":
                conversion_table()
        elif choice == "9":
                make_initialism()
        elif choice == "10":
                file_in_caps()
        elif choice == "11":
            total_spending()
        elif choice == "12":
            name_to_number()
        elif choice == "13":
            rainfall_chart()
        elif choice == "14":
            rainfall_graphics()
        elif choice == "15":
            five_click_stick_figure()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
menu()