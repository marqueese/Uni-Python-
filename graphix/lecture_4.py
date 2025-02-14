def mystery(n, word): #thats racist
    result = ""
    for i in range(n):
        part = word * i
        result += part
        return len(result) #won't return anything in the loop

def main():
    print(mystery(4, "hi"))

def is_even():
    number = int(input("Input a number: "))

    return number

def check():
        number = is_even()
        if number % 2 == 0:
            print("Shits good")
        else:{
            print("not good")
        }

def heating_bill():

    temp = input("put the temp in : ")

    if temp < 20:{
        print("Turn the heating on")
    }
    elif temp <23:{
        print("Nothing happened")
    }
    elif temp <25:{
        print("Cooling down")
    }
    elif temp > 25:{
        print("start fan")
    }
    else:{
        print("You Broke it")
    }

