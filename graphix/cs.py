from graphix import *

def size():
    print("1: 5 x 5")
    print("2: 7 x 7")
    print("3: 9 x 9")

    while True:
        screen_size = int(input("What size will the screen be: "))

        if screen_size == 1:
            return 500, 5
        elif screen_size == 2:
            return 700, 7
        elif screen_size == 3:
            return  900, 9
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

        color_list = {
            '1':'red', '2': 'green', '3': 'blue' ,
            '4': 'orange', '5': 'purple', '6': 'magenta'
        }

        color_name = color_list[color_choice]

        if color_name in chosen_color:
            print("You have already chosen this color")
        else:
            chosen_color.append(color_name) # set a variable for the color to add

    return chosen_color #colors should be stored in this

def create_grid(colors, grid_size):
    color_grid = []
    arrangement = []

    for rows in range (grid_size):
        color_row = []
        arrangement_rows = []
        for column in range (grid_size): # read these comments beofre you try to change things
            if rows == column or rows + column == grid_size -1: # eg 1 == 2 or 1 + 2 == 5-1 diagonal and reversed diagonal
                color_row.append(colors[0])
                #arrangement_rows.append('i')
            elif rows < column and rows + column < grid_size -1: # eg 3 < 4 and 1 + 2 < 5 -1 top section
                color_row.append(colors[1])
                #arrangement_rows.append('f')
            elif rows > column and rows + column > grid_size -1: # bottom section cant be bothered to use example
                color_row.append(colors[1])
                #arrangement_rows.append('f') # sort this out when i can be bothered
            else:
                color_row.append(colors[2])
                arrangement_rows.append('p')
        color_grid.append(color_row)
        arrangement.append(arrangement_rows)


    return color_grid, arrangement

def draw(window, grid, square_width): # call this one to make stuff

    rows, columns = len(grid), len(grid[0])# specify this when making the graph thingy

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

if __name__ == "__main__":
    relative_size, grid_size = size()
    chosen_colors = colors()

    colors, arranged = create_grid(chosen_colors, grid_size)

    window = Window("Grid thingy", relative_size, relative_size)
    draw(window, colors, relative_size // grid_size)

    window.get_mouse()
    window.close()
