from graphix import *

def personal_greeting():
        name = input("What is your name: ")
        print("Well hello there,", name, "How are you today?")

def formal_name():
        fname = input("What is your forename: ")
        sname = input("What is your surname: ")

        f_letter = fname[0]

        print(f_letter.upper(),".",sname)

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    ounces = round(ounces, 2)
    print("The weight of",kilos,"kilos in ounces is:",ounces)

def generate_email():
        fname = input("What is your forename: ")
        sname = input("What is your surname: ")
        year = input("When will be your first year in university: ")

        fname = fname[0]
        sname = sname[0:4]
        year = year[2:4]

        print("Your uni email is")
        print(f"{sname}.{fname}.{year}@myport.ac.uk")

def grade_test():
        grades = "FFFCCBBAAA"

        mark = int(input("Enter your mark (0-10): "))
        grade = grades[max(0, min(10, mark))]
        print(f"Your grade is: {grade}")

def graphic_letters():
        window = Window("The Graph of stuff", 500, 500)

        word = input("Enter a word: ")
        variable = 0

        for ch in word:

                letter = word[variable]

                click = window.get_mouse()
                Letter_Display = Text(click, letter)
                Letter_Display.draw(window)

                variable += 1
        window.close()

def sing_a_song():
        word = input("Enter a word: ")
        wps = int(input("how many times a line: "))
        rows = int(input("how many rows of this: "))

        for words in range (rows):
                print(f"{word * wps}")

def conversion_table():
        gbp = 1
        euro = 1.17

def menu():
    while True:
        print("\nPlease select an option:")
        print("1. Personal Greeting")
        print("2. Formal name")
        print("3. Kilos to ounces")
        print("4. Generate email")
        print("5. Grade test")
        print("6. Letter thingy")
        print("7. Sing a song ")
        print("7. Conversion Table ")
        print("9. Exit")

        choice = input("\nEnter the number of your choice: ")

        if choice == '1':
            personal_greeting()
        elif choice == '2':
            formal_name()
        elif choice == '3':
            kilos_to_ounces()
        elif choice == "4":
                generate_email()
        elif choice == "5":
                grade_test()
        elif choice == "6":
                graphic_letters()
        elif choice == "7":
                sing_a_song()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
menu()
