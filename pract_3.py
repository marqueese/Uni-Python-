from subprocess import check_output

from graphix import *

def draw_stick_figure():
    window = Window("The Graph of stuff", 500, 500)
    head = Circle(Point(200, 120), 40)
    head.draw(window)

    body = Line(Point(200, 160), Point(200, 240))
    body.draw(window)

    left_arm = Line(Point(200, 190), Point(140, 160))
    left_arm.draw(window)

    right_arm = Line(Point(200, 190), Point(260, 160))
    right_arm.draw(window)

    left_leg = Line(Point(200, 240), Point(160, 300))
    left_leg.draw(window)

    right_leg = Line(Point(200, 240), Point(240, 300))
    right_leg.draw(window)

    window.get_mouse()
    window.close()

def draw_circle():
    radius = int(input("Input the radius in the form of an integer: "))
    diameter = radius * 2

    window = Window("The circle maker", 500, 500)
    circle = Circle(Point(250, 250), diameter)
    circle.draw(window)

    window.get_mouse()
    window.close()

def draw_archery_target():
    window = Window("archery target", 500, 500)

    main_circle = Circle(Point(250, 250), 240)
    main_circle.fill_colour = "blue"
    main_circle.draw(window)

    secondary_circle = Circle(Point(250, 250), 160)
    secondary_circle.fill_colour = "red"
    secondary_circle.draw(window)

    final_circle = Circle(Point(250, 250), 80)
    final_circle.fill_colour = "yellow"
    final_circle.draw(window)

    window.get_mouse()
    window.close()

def draw_rectangle():
    width = int(input("What is the width of the rectangle: "))
    length = int(input("What is the length of the rectangle: "))

    start_y = (500 - width) // 2
    start_x = (500 - length) // 2
    end_y = start_y + width
    end_x = start_x + length

    window = Window("rectangle thingy", 500, 500)
    rectangle = Rectangle(Point(start_x, start_y), Point(end_x, end_y))
    rectangle.draw(window)

    window.get_mouse()
    window.close()

def blue_circle():
    window = Window("Circle Thingy", 500, 500)

    window.get_mouse()
    circle = Circle(Point(250, 250), 100)
    circle.fill_colour = "blue"
    circle.draw(window)

    window.get_mouse()
    window.close()

def draw_line():
    window = Window("Lines", 500, 500)
    start_point = window.get_mouse()
    end_point = window.get_mouse()

    line = Line(start_point, end_point)
    line.draw(window)

    window.get_mouse()
    window.close()


def ten_strings():
    window = Window("piece o crap", 500, 500)

    for i in range(10):
        input_box = Entry(Point(250, 30), 30)
        input_box.draw(window)

        click_point = window.get_mouse()

        message = Text(click_point, input_box.text)#this is useful dont be a dumbass
        message.draw(window)

        input_box.undraw()

    window.get_mouse()
    window.close()

def ten_coloured_rectangles():
    window = Window("rectangle thingy", 500, 500)

    for i in range(10):
        input_box = Entry(Point(250, 30), 30)
        input_box.text = "blue"
        input_box.draw(window)

        x = window.get_mouse()
        y = window.get_mouse()
        color = input_box.text

        rectangle = Rectangle(x , y)
        rectangle.fill_colour = color
        rectangle.draw(window)

    window.get_mouse()
    window.close()

def menu():
    while True:
        print("\nPlease select an option:")
        print("1. Draw Stick Figure")
        print("2. Draw Circle")
        print("3. Draw Archery Target")
        print("4. Draw Rectangle")
        print("5. Blue Circle")
        print("6. Draw Line")
        print("7. Ten Strings")
        print("8. 10 Coloured Rectangles")
        print("9. Exit")

        choice = input("\nEnter the number of your choice: ")

        if choice == '1':
            draw_stick_figure()
        elif choice == '2':
            draw_circle()
        elif choice == '3':
            draw_archery_target()
        elif choice == '4':
            draw_rectangle()
        elif choice == '5':
            blue_circle()
        elif choice == '6':
            draw_line()
        elif choice == '7':
            ten_strings()
        elif choice == "8":
            ten_coloured_rectangles()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

menu()
