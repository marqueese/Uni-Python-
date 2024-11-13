def fast_food_order_price():
    price = float(input("How much is the order: :"))
    delivery = 0

    if price < 20:
        delivery = 2.50

    price_total = price + delivery

    print(f"Your order total is {price_total}")

def what_to_do_today():
    temp = float(input("What's the temperature in °C: "))

    if temp > 50:
        print("You're dead just accept it")
    elif temp > 25:
        print("Go for a swim in the sea")
    elif 10 <= temp <= 25:
        print("Go shopping in Gunwharf Quays")
    elif temp < 10:
        print("Stay indoors and watch a film")


def display_square_routes(start, end):
    for i in range (start, end):
        sqrt = i **0.5


display_square_routes(4, 7)