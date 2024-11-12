import math

from graphix import *
from math import *

#circle calculations
def circle_circ(radius):
    return 2 * pi * radius

def circ_area(radius):
    return pi * radius ** 2

def main_circles():
    radius = float(input("what is the radius of the circle: "))
    area = circle_circ(radius)
    circ = circ_area(radius)
    print(f"The area is {area} and the circumference is {circ} ")


#drawing stuff
def draw():
    circle_1 = Circle(Point(150, 150), 120)
    circle_1.fill_colour="white"

    circle_2 = Circle(Point(150, 150), 60)
    circle_2.fill_colour ="brown"

    circle_3 = Circle(Point(150, 150), 30)
    circle_3.fill_colour = "black"

    return circle_1, circle_2, circle_3

def draw_second_eye():
    circle_4 = Circle(Point(390, 150), 120)
    circle_4.fill_colour="white"

    circle_5 = Circle(Point(390, 150), 60)
    circle_5.fill_colour ="brown"

    circle_6 = Circle(Point(390, 150), 30)
    circle_6.fill_colour = "black"

    return circle_4, circle_5, circle_6

def drawing():
    window = Window("circle" , 500, 500)

    circle_1, circle_2 , circle_3 = draw()

    circle_1.draw(window)
    circle_2.draw(window)
    circle_3.draw(window)

    window.get_mouse()
    window.close()

def draw_block_of_stars():
    wps = int(input("how many times a line: "))
    rows = int(input("how many rows of this: "))

    return wps, rows

def main_star_block():
    char = "*"
    rows , wps = draw_block_of_stars()

    for words in range(rows):
        print(f"{char * wps}")


def draw_an_e():
    char = "*"
    wps, rows = draw_block_of_stars()

    print(char * wps)

    for i in range(rows - 2):
        print(char)

    print(char * (wps // 2))

    for i in range(rows - 2):
        print(char)

    print(char * wps)

def draw_a_pair_of_eyes():
    window = Window("circle" , 550, 500)

    circle_1, circle_2, circle_3 = draw()
    circle_4, circle_5, circle_6 = draw_second_eye()

    circle_1.draw(window)
    circle_2.draw(window)
    circle_3.draw(window)
    circle_4.draw(window)
    circle_5.draw(window)
    circle_6.draw(window)

    window.get_mouse()
    window.close()

def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def display_distance_between_points():
    window = Window("circle" , 500, 500)

    p1 = window.get_mouse()
    p2 = window.get_mouse()

    rect = Rectangle(Point(p1.x , p1.y), Point(p2.x, p2.y))
    rect.draw(window)

    window.get_mouse()
    rect.undraw()

    text = Text(Point(250, 250), "Click again to find the distance between\n")
    text.draw(window)

    window.get_mouse()
    text.undraw()

    distance = distance_between_points(p1, p2)
    message = f"The distance between points is: {distance}"
    text = Text(Point(250, 250), message)
    text.draw(window)

    window.get_mouse()
    window.close()

def draw_blocks(width1, width2, width3, width4, height):
    for _ in range(height):
        line = " " * width1 + "*" * width2 + " " * width3 + "*" * width4
        print(line)

def draw_letter_a():
    draw_blocks(1, 8, 0, 0, 2)
    draw_blocks(1, 2, 4, 2, 2)
    draw_blocks(1, 8, 0, 0, 2)
    draw_blocks(1, 2, 4, 2, 3)

draw_a_pair_of_eyes()
