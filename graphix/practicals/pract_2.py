##import stuff
import math
from _ast import While
from math import pi

def speed_calculator():
    distance = float(input("how far did you travel in kilometers: "))
    duration = float(input("how long did you travel for in hours: "))

    ##calculate speed
    speed = distance / duration
    speed = round(speed, 2)
    print("your average speed was ", speed, "kmph")

def circumference_of_circle():
    radius = float(input("what is the radius of your circle: "))

    circumference = 2 * pi * radius

    print("the circumference of the circle is: ", circumference)

def area_of_circle():
    radius = float(input("what is the radius of your circle: "))
    area = pi * radius ** 2

    print("the area of your circle is: ", area)

def cost_of_pizza():
    diameter = float(input("what is the diameter of your pizza in cm: "))
    radius = diameter / 2
    area = pi * radius ** 2
    cost = area * 3.5

    total = cost / 100
    total = round(total, 2)
    print("your pizza will cost £", total)

def slope_of_line():
    x1 = float(input("what is your first point on the x-axis: "))
    y1 = float(input("what is your first point on the y-axis: "))
    x2 = float(input("what is your second point on the x-axis: "))
    y2 = float(input("what is your second point on the x-axis: "))

    slope = (y2 / y1) / (x2 - x1)

    print("the slope of the line that connects them is")

def distance_between_points():
    x1 = float(input("what is your first point on the x-axis: "))
    y1 = float(input("what is your first point on the y-axis: "))
    x2 = float(input("what is your second point on the x-axis: "))
    y2 = float(input("what is your second point on the x-axis: "))

    distance_x = x1 - x2
    distance_y = y1 - y2

    print("the distance between the 2 x axis marks is ", distance_x,
          "\n and the distance between items on the y axis is ", distance_y)

def travel_statistics():
    speed = int(input("What was you average speed: "))
    time = int(input("in exact hours how long did you travel for : "))

    distance= speed/time

    fuel_consumption = distance / 5

    print("You traveled ",distance, "km and used",fuel_consumption," Litres of fuel",)

def sum_of_squares():
    number = int(input("Enter your number: "))
    x = 0
    for i in range (number +1):
        x += i ** 2

    print("the total is ",x)

def average_of_numbers():
    amount = int(input("How many numbers will you be submitting: "))
    x = 0
    for i in range(amount):
        number = int(input("Select a whole number: "))
        x = x + number

    average = x / amount
    print("your average is ",average)

def fibonacci():
    number = int(input("Pick a number: "))

    previous_number = 0
    current_number = 1

    for i in range(2, number + 1):
        next_number = previous_number + current_number
        previous_number = current_number
        current_number = next_number
        print(current_number)

def counting_coins():
    ammount = int(input("How much money do you have (in pence): "))

    coin_types = {
    "£2" : 200,
    "£1" : 100,
    "50p": 50,
    "20p": 20,
    "10p": 20,
    "5p" : 5,
    "2p" : 2,
    "1p" : 1
    }

    for coin, coin_value in coin_types.items():
        coin_ammount = ammount // coin_value #intiger division
        ammount &= coin_value # add the remainder to it
        print(f"{coin_ammount} * {coin}")

while True:
    print("\nwhat function is being run")
    print("1: Speed calculator")
    print("2: Circumference of a circle")
    print("3: Area of a circle")
    print("4: Cost of pizza")
    print("5: slope of line")
    print("6: distance between points")
    print("7: travel statistics")
    print("8: sum of squares")
    print("9: average of numbers")
    print("10: fibonacci")
    print("11: counting coins")
    choice = int(input("Choose a function number: "))

    if choice == 1:
        speed_calculator()

    if choice == 2:
        circumference_of_circle()

    if choice == 3:
        area_of_circle()

    if choice == 4:
        cost_of_pizza()

    if choice == 5:
        slope_of_line()

    if choice == 6:
        distance_between_points()

    if choice == 7:
        travel_statistics()

    if choice == 8:
        sum_of_squares()

    if choice == 9:
        average_of_numbers()

    if choice == 10:
        fibonacci()

    if choice == 11:
        counting_coins()