from graphix import *

def size():
    print("1: 5 x 5")
    print("2: 7 x 7")
    print("3: 9 x 9")

    while True:
        screen_size = int(input("What size will the screen be: "))

        if screen_size == 1:
            return 500
        elif screen_size == 2:
            return 700
        elif screen_size == 3:
            return  900
        else:
            print("What you have entered is not an option retry")


def colors():
    print("1: red")
    print("2: green")
    print("3: blue")
    print("4: orange")
    print("5: magenta")
    print("6: purple")

    chosen_color = [] #store colors in this list and use them later

    while len(chosen_color) < 3: # runs until 3 colors are chosen
        color_choice  = input("Pick a color you want: ")

        if not color_choice.isdigit():
            print("enter a number from 1-6")
            continue

        if color_choice < '1' or color_choice > '6':
            print("Enter a number from the list provided")
            continue

        color_name = None #default value or stuff breaks
        if color_choice == '1':
            color_name = "red"
        elif color_choice == '2':
            color_name = "green"
        elif color_choice == '3':
            color_name = "blue"
        elif color_choice == '4':
            color_name = "orange"
        elif color_choice == '5':
            color_name = "magenta"
        elif color_choice == '6':
            color_name = "purple"

        if color_name in chosen_color:
            print("You have already chosen this color")
        else:
            chosen_color.append(color_name) # set a variable for the color to add

    return chosen_color #colors should be stored in this


def draw(window, grid, square_width, screen_size): # call this one to make stuff

    rows, columns = screen_size, screen_size # specify this when making the graph thingy

    for row in range(rows):
        for column in range (columns):
            x1 = column * square_width
            y1 = row * square_width
            x2 = x1 + square_width
            y2 = y1 + square_width

            cell_color = grid[row][column]

            rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
            rectangle.fill_colour = cell_color
            rectangle.draw(window)


def list_1():
    chosen_colors = colors()

    color_grid = [# where colors are
        [chosen_colors[0], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[0]],
        [chosen_colors[2], chosen_colors[0], chosen_colors[1], chosen_colors[0], chosen_colors[2]],
        [chosen_colors[2], chosen_colors[2], chosen_colors[0], chosen_colors[2], chosen_colors[2]],
        [chosen_colors[2], chosen_colors[0], chosen_colors[1], chosen_colors[0], chosen_colors[2]],
        [chosen_colors[0], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[0]]]

    arrangement = [ # determine where items go
        ["i", "i", "i", "i", "i"],
        ["i", "f", "p", "f", "i"],
        ["i", "p", "f", "p", "i"],
        ["i", "f", "p", "f", "i"],
        ["i", "i", "i", "i", "i"]]

    window = Window("small grid",relative_size, relative_size)

    draw(window, color_grid, 100, 5)
    #patches(window, arrangement, 100)
    window.get_mouse()
    window.close()

def list_2():
    chosen_colors = colors()

    color_grid = [# where colors are
        [chosen_colors[0], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[0]],
        [chosen_colors[2], chosen_colors[0], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[0], chosen_colors[2]],
        [chosen_colors[2], chosen_colors[2], chosen_colors[0], chosen_colors[1], chosen_colors[0], chosen_colors[2], chosen_colors[2]],
        [chosen_colors[2], chosen_colors[2], chosen_colors[2], chosen_colors[0], chosen_colors[2], chosen_colors[2], chosen_colors[2]],
        [chosen_colors[2], chosen_colors[2], chosen_colors[0], chosen_colors[1], chosen_colors[0], chosen_colors[2], chosen_colors[2]],
        [chosen_colors[2], chosen_colors[0], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[0], chosen_colors[2]],
        [chosen_colors[0], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[1], chosen_colors[0]]
        ]

    arrangement = [ # determine where items go
        ["i", "i", "i", "i", "i", "i", "i"],
        ["i", "f", "p", "p", "p", "f", "i"],
        ["i", "p", "f", "p", "f", "p", "i"],
        ["i", "p", "p", "f", "p", "p", "i"],
        ["i", "p", "f", "p", "f", "p", "i"],
        ["i", "f", "p", "p", "p", "f", "i"],
        ["i", "i", "i", "i", "i", "i", "i"],
    ]

    window = Window("small grid",relative_size, relative_size)

    draw(window, color_grid, 100, 7)
    #patches(window, arrangement, 100)
    window.get_mouse()
    window.close()

if __name__ == "__main__":
    relative_size = size()

    while True:
        if relative_size == 500:
            list_1()
        if relative_size == 700:
            list_2()
        else:
            print("i havent made the rest yet")

