import math
from math import pi

def biscuit_cutting():
    
    diameter = float(input("What is the diameter of each biscuit in cm: "))
    length = int(input("How many biscuts are along the length of the tray: "))
    width = int(input("how many biscuts are along the width of the tray: "))
    
    #get radius to work out area of each biscut
    radius = diameter / 2
    area = pi * (radius ** 2)
    
   
    #area of the mixture
    mixture_length = length * diameter
    mixture_width = diameter * width
    
    #area variable
    mixture_area = mixture_length * mixture_width
    
    #mixture used
    biscuit_number = length * width
    mixture_used = biscuit_number * area
    mixture_remaining = mixture_area - mixture_used
    
    #how many can be made
    extra_biscuits = mixture_remaining / area
    extra_biscuts = int(extra_biscuits)
    extra_biscuts = round(extra_biscuts, 0)
                
    print("the radius of each biscuit is ",radius)
    print("the area of each biscuit is ",area)
    print("the full number of space available is ",mixture_area,"cm^2")
    
    if extra_biscuits > 0:
        print("with the remaining mixture you can make",extra_biscuts,"more biscuits")
    else:
        print("there isn't not enough mixture for any more biscuts")

from graphix import *

def clicking():
    window = Window("Graph", 500, 500)
    
    click = window.get_mouse()  # Get the initial click location to set message position
    i = 1
    
    # Create the Text object at the clicked position with the initial message
    message = "H" + "i" * i
    text = Text(click, message)
    text.draw(window)
    
    # Update the text message in place on each iteration
    for i in range(2, 10):
        message = "H" + "i" * i
        text.set_message(message)  # Update the text content
        window.get_mouse()  # Wait for another click to update

    window.get_mouse()  # Wait for a final click to close
    window.close()

clicking()
