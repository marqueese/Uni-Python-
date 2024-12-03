from random import random
import math

def get_inputs():
    num_walks = int(input("How many random walks to take? "))
    num_steps = int(input("How many steps for each walk? "))
    return num_walks, num_steps

def take_a_walk(num_steps):
    x, y = 0, 0
    for _ in range(num_steps):
        direction = random()
        if direction < 0.25:
            y += 1
        elif direction < 0.5:
            x += 1
        elif direction < 0.75:
            y -= 1
        else:
            x -= 1
    return x, y

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def take_walks(num_walks, num_steps):
    total_distance = 0
    for _ in range(num_walks):
        x, y = take_a_walk(num_steps)
        distance = distance_between_points(0, 0, x, y)
        total_distance += distance
    return total_distance / num_walks

def print_expected_distance(average_distance):
    print("The expected distance from the start point is", average_distance)

def main():
    num_walks, num_steps = get_inputs()
    average_distance = take_walks(num_walks, num_steps)
    print_expected_distance(average_distance)

main()
