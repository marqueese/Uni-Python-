# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print("The weight in ounces is:",ounces)
    
def say_hello():
    print("hello  there")
    
def say_goodbye():
    print("Goodbye")

def list_of():#run the list 5 times
    for i in range(5):
        print(i)
        
def count():
    for number in range(10):#run the loop 10 times
        print("The number is: ", number)
        
def say_name():
    print("Marcus")
    
def say_hello_2():
    print("Hello")
    print("World")
    
def dollars_to_pounds():
    ammount = float(input("How much currency is being converted: "))
    Rate = 1.35
    conversion = (Rate * ammount)
    rounded = round(conversion, 2)#set the number of decimal places here
    print("£",rounded)

def sum_and_difference():
    num_1 = int(input("enter your first number: "))
    num_2 = int(input("enter your second number: "))
    sum_of = (num_1 + num_2)
    print("the sum of the 2 is: ",sum_of)
    difference = (num_1 - num_2)
    print("the difference between them is: ",difference)
    
def change():
    one_pence = int(input("How many one pence pieces would you like: "))
    two_pence = int(input("How many two pence pieces would you like: "))
    five_pence = int(input("How many five pence pieces would you like: "))

    two_pence_total = (two_pence * 2)#adjust for 2 pence pieces
    five_pence_total = (five_pence * 5)#adjust for 5 pence pieces

    total = (one_pence + two_pence_total + five_pence_total)
    print("Your total ammount of change is: ", total)

def hello_loop():
    for i in range (10):
        print("Hello World \n")

def zoom_zoom():
    for number in range(10):  # run the loop 10 times
        print("zoom", number)

def count_too():
    my_number = int(input("What number am i counting too"))
    get_number = (my_number + 1)

    for get_number in range(1, get_number):
        print(get_number)

def weights_table():
    i = 10
    while (i < 101):
        ounces = 35.274 * i
        rounded = round(ounces, 2)  # set the number of decimal places here
        print(i,"KG is",rounded,"ounces")
        i = i + 10

weights_table()

def future_value():
    deposit = float(input("How much will you deposit"))
    years = int(input("how many years will this be sat in the bank for"))
    years_total = years + 1
    balance = deposit
    for i in range(1,years_total):

        balance = balance * 1.035
        rounded = round(balance, 2)
        print ("year",i,"balance is",rounded)

