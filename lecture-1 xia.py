#import the random function
import random #will remain grey until used

print("input 3 numbers in and i will find the average")

#use these if you want to select the numbers
first = float(input("input first number: "))
second = float(input("input second number: "))
third = float(input("input third number: "))

#use this for random numbers and determine the range\
#first = random.randint(1, 100)
#second = random.randint(1, 100)
#third = random.randint(1, 100)

#divide by 3 to get the average
average = (first + second + third) / 3

#if the average is above 50 run this
if average > 50:
    print("the average of your numbers is: ", average)  #display the average
    print("higher end of the spectrum ")
#if not run this
else:
    print("the average of your numbers is: ", average)  #display the average
    print("tristan leave my keyboard alone")
