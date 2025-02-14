import random

def main():
    print("Flipping coins for some reason")
    flips = get_inputs()
    heads, tails = simulate_flips(flips)
    display_results(heads, tails)

def get_inputs():
    flips = int(input("How many times is the coin being flipped? "))
    return flips

def simulate_flips(flips):
    heads = 0
    tails = 0

    for _ in range(flips):
        random_number = random.randint(1, 2)
        if random_number == 1:
            heads += 1
        else:
            tails += 1

    return heads, tails

def display_results(heads, tails):
    print(f"Your ratio of heads to tails flips was {heads}:{tails}")

main()
