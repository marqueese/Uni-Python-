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
    print("1: red\n2: green\n3: blue\n4: orange\n5: magenta\n6: purple")
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


def patch_1(length, x, y, window, color):
    for i in range(0, length, 20):
        line1 = Line(Point(x , y + i), Point(i + x, y))
        line1.draw(window)
        line1.fill_colour = color

        line2 = Line(Point(x+ i, y + length), Point(x + length, y+ i))
        line2.draw(window)
        line2.fill_colour = color

    for i in range(0, length, 20):
        line3 = Line(Point(x,y + length - i), Point(x+ i, y+ length))
        line3.draw(window)
        line3.fill_colour = color

        line4 = Line(Point(x+ i, y), Point(x+ length, y+ length - i))
        line4.draw(window)
        line4.fill_colour = color


def patch_2(base, height, rows , cols, window, x ,y, color):
# fix the shapes eventually
    start_x1 , start_y1 = x + 10, y
    start_x2 , start_y2 = x + base + 10, y
    start_x3 , start_y3 = 10 + x + base // 2, y + height

    for row in range(rows):
        offset = -(base // 2) if row % 2 != 0 else 0 # if the row number has no remainders shift it by the base

        x1_1, x2_1, x3_1 = start_x1 + offset, start_x2 + offset, start_x3 + offset

        for column in range(cols):

            x1 = Point(x1_1, start_y1)
            x2 = Point(x2_1, start_y2)
            x3 = Point(x3_1, start_y3)

            triangle = Polygon([x1, x2, x3])
            triangle.draw(window)
            triangle.fill_colour = color

            x1_1 += base
            x2_1 += base
            x3_1 += base

        start_y1 += height
        start_y2 += height
        start_y3 += height


def create_grid(colors, grid_size):
    color_grid = []

    for rows in range (grid_size):
        color_row = []
        for column in range (grid_size): # read these comments beofre you try to change things
            if rows == column or rows + column == grid_size -1: # eg 1 == 2 or 1 + 2 == 5-1 diagonal and reversed diagonal
                color_row.append(colors[0])
            elif rows < column and rows + column < grid_size -1: # eg 3 < 4 and 1 + 2 < 5 -1 top section
                color_row.append(colors[1])
            elif rows > column and rows + column > grid_size -1: # bottom section cant be bothered to use example
                color_row.append(colors[1])
            else:
                color_row.append(colors[2])
        color_grid.append(color_row)

    return color_grid


def patch_grid(grid_size):
    arrangement = []

    for row in range(grid_size):
        arrangement_row = []
        for column in range(grid_size):
            if row == 0 or row == grid_size - 1 or column == 0 or column == grid_size - 1:
                arrangement_row.append('o')
            elif row == column or row + column == grid_size - 1:
                arrangement_row.append('p')
            else:
                arrangement_row.append('f')
        arrangement.append(arrangement_row)

    return arrangement


def draw(window, grid, square_width, arrangement): # call this one to make stuff
    rows, columns = len(grid), len(grid[0])# specify this when making the graph thingy

    for row in range(rows):
        for column in range (columns):
            x1 = column * square_width
            y1 = row * square_width
            x2 = x1 + square_width
            y2 = y1 + square_width

            cell_color = grid[row][column]
            cell_type = arrangement[row][column]

            if cell_type == 'p':
                patch_1(100, x1, y1, window, cell_color)
            elif cell_type == 'f':
                patch_2(22, 20, 5, 4, window, x1, y1, cell_color)# fuck YOU STUPID BITCH COORDINATES
            else:
                rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
                rectangle.fill_colour = cell_color
                rectangle.draw(window)


if __name__ == "__main__":
    #import the stuff
    relative_size, grid_size = size()
    chosen_colors = colors()
    arrangement_grid = patch_grid(grid_size)
    colors = create_grid(chosen_colors, grid_size)

    #draw the stuff
    window = Window("Grid thingy", relative_size, relative_size)
    draw(window, colors, relative_size // grid_size,arrangement_grid)

    window.get_mouse()
    window.close()