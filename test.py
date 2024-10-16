##import stuff
import math
from math import pi

def speed_calculator():
    distance = float(input("\nhow far did you travel in kilometers: "))
    duration = float(input("how long did you travel for in hours: "))

    ##calculate speed
    speed = distance / duration
    speed = round(speed, 2)
    print("your average speed was ", speed, "kmph")

def circumference_of_circle():
    radius = float(input("\nwhat is the radius of your circle: "))

    circumference = 2 * pi * radius

    print("the circumference of the circle is: ",circumference)

def area_of_circle():
    radius = float(input("\nwhat is the radius of your circle: "))
    area = pi * radius** 2

    print("the area of your circle is: ", area)

def cost_of_pizza():
    diameter = float(input("\nwhat is the diameter of your pizza in cm: "))
    radius = diameter / 2
    area = pi * radius ** 2
    cost = area * 3.5

    total = cost / 100
    total = round(total , 2)
    print("your pizza will cost £",total)

def slope_of_line():
    x1 = float(input("\nwhat is your first point on the x-axis: "))
    y1 = float(input("what is your first point on the y-axis: "))
    x2 = float(input("what is your second point on the x-axis: "))
    y2 = float(input("what is your second point on the x-axis: "))

    slope = (y2 / y1) / (x2 - x1)

    print("the slope of the line that connects them is ",slope)

print("What function is being run")
print("1: Speed calculator")
print("2: Circumference of a circle")
print("3: Area of a circle")
print("4: Cost of pizza")
print("5: Slope of line")
print("6: Exit\n")

while True:
    choice = input("Choose a function number: ")

    if choice == "1":
        speed_calculator()
    elif choice == "2":
        circumference_of_circle()
    elif choice == "3":
        area_of_circle()
    elif choice == "4":
        cost_of_pizza()
    elif choice == "5":
        slope_of_line()
    elif choice == "6":
        exit()
    else:
        print("Idiot, try again...")
