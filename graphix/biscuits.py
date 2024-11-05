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
    
    # Get the initial click location for the text position
    click_x, click_y = window.get_mouse()  # Initial click coordinates
    i = 1
    
    # Create the first text object at the clicked position
    message = "H" + "i" * i
    text = Text((click_x, click_y), message)
    text.draw(window)
    
    # Update the text each time a click occurs
    for _ in range(9):  # Repeat 9 more times to reach 10 clicks
        i += 1
        message = "H" + "i" * i
        
        # Undraw the previous text and create a new one at the same coordinates
        text.undraw()
        text = Text((click_x, click_y), message)
        text.draw(window)
        
        window.get_mouse()  # Wait for the next click

    window.get_mouse()  # Wait for a final click to close
    window.close()

clicking()
