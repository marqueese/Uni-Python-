def spacing():

    user_input = input("enter a word: ")
    result = ""

    for ch in user_input:
        result += ch + " "
    print(result)


def reverse():
    user_input = input("enter a word: ")
    result = ""

    for ch in user_input:
        result = user_input[::-1]
    print(result)


def caesar_shift():

    user_input = input("enter a word: ")
    shift = 1
    result = ""

    for ch in user_input:
        shifted = chr(((ord(ch) - ord("a") + shift) % 26) +ord("a"))
        result += shifted
    print(result)

caesar_shift()

