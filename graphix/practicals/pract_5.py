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
def draw_circle(x, y, radius, color, window):
    circle = Circle(Point(x, y), radius)
    circle.fill_colour = color
    circle.draw(window)
    
    
def draw_brown_eye(x, y, window):
    draw_circle(150, 150, 120, "white", window)
    draw_circle(150, 150, 60, "brown", window)
    draw_circle(150, 150, 30, "black", window)

    window.get_mouse()
    window.close()
    
def draw_pair_of_eyes():
    window = Window("eyes again" , 500, 500)
    draw_brown_eye(40, 40, window)
    draw_brown_eye(150, 150, window)


def draw_block_of_stars(width, height):
    char = "*"
    for words in range(width):
        print(f"{char * height}")


def draw_an_e():
    draw_block_of_stars(2, 8)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(2, 8)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(2, 8)

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

def draw_blocks(width1, width2, width3, width4, height):#spacing from column, number per line, spacing, spacing size, number of lines
    for _ in range(height):
        line = " " * width1 + "*" * width2 + " " * width3 + "*" * width4
        print(line)

def draw_letter_a():
    draw_blocks(1, 8, 0, 0, 2)
    draw_blocks(1, 2, 4, 2, 2)
    draw_blocks(1, 8, 0, 0, 2)
    draw_blocks(1, 2, 4, 2, 3)

