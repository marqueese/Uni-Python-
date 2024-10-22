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

counting_coins()