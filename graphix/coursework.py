from graphix import *

def size():
    print("1: 5 x 5\n2: 7 x 7\n3: 9 x 9")
    while True:
        screen_size = input("What size will the screen be: ")

        if not screen_size.isdigit():
            print("enter a number from 1-3")
            continue

        if screen_size  <'1' or screen_size > '3':
            print("Enter a number from the list provided")
            continue

        if screen_size == '1':
            return 500, 5
        elif screen_size == '2':
            return 700, 7
        elif screen_size == '3':
            return  900, 9
        else:
            print("What you have entered is not an option retry")


def colors():
    print("1: red\n2: green\n3: blue\n4: orange\n5: magenta\n6: purple")
    chosen_color = [] #store colors in this list and use them later

    while len(chosen_color) < 3: # runs until 3 colors are chosen
        color_choice  = input("Pick a color you want: ")

        if not color_choice.isdigit():
            print("Enter a number from 1-6")
            continue

        if color_choice < '1' or color_choice > '6':
            print("Enter a number from the list provided")
            continue

        color_list = {
            '1':'red', '2': 'green', '3': 'blue' ,'4': 'orange', '5': 'purple', '6': 'magenta'
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
        line2 = Line(Point(x+ i, y + length), Point(x + length, y+ i))
        line3 = Line(Point(x, y + length - i), Point(x + i, y + length))
        line4 = Line(Point(x + i, y), Point(x + length, y + length - i))

        line1, line2, line3, line4.draw(window)
        line1, line2, line3, line4.fill_colour= color, color, color, color
        line1, line2, line3, line4.outline_width = 2, 2, 2, 2


def patch_2(base, height, rows , cols, window, x ,y, color):
    start_x1 , start_y1 = x , y
    start_x2 , start_y2 = x + base, y
    start_x3 , start_y3 = x + base // 2, y + height

    for row in range(rows):
        offset = -(base // 2) if row % 2 != 0 else 0 # if the row number has no remainders shift it by the base
        x1_1, x2_1, x3_1 = start_x1 + offset, start_x2 + offset, start_x3 + offset

        for column in range(cols):

            x1, x2, x3 = Point(x1_1, start_y1), Point(x2_1, start_y2), Point(x3_1, start_y3)

            triangle = Polygon([x1, x2, x3])
            triangle.draw(window)
            triangle.fill_colour = color

            x1_1, x2_1 , x3_1 = x1_1 +  base, x2_1 + base , x3_1 + base

        if row % 2 != 1:
            right_half = Polygon([Point(x1_1 - base // 2 - 90, start_y1),Point(x1_1- 90, start_y1),
                                  Point(x1_1 - base // 2 - 90, start_y1 + height)])
            right_half.draw(window)
            right_half.fill_colour = color

        elif row % 2 != 0:
            left_half = Polygon([Point(start_x1 + 80, start_y1), Point(80 + start_x1 + base // 2, start_y1 + height),
                                 Point(80 + start_x1 + base // 2, start_y1)])
            left_half.draw(window)
            left_half.fill_colour = color

        start_y1, start_y2, start_y3 = start_y1 + height, start_y2 + height, start_y3 + height


def create_grid(colors, grid_size):
    color_grid = []

    for rows in range (grid_size):
        color_row = []
        for column in range (grid_size): # read these comments before you try to change things
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
                arrangement_row.append('f')
            else:
                arrangement_row.append('p')
        arrangement.append(arrangement_row)
    return arrangement


def draw(window, grid, square_width, arrangement, stored_objects): # call this one to make stuff
    rows, columns = len(grid), len(grid[0])# specify this when making the graph thingy
    for row in range(rows):
        for column in range (columns):
            x1, y1 = column * square_width, row * square_width
            x2, y2 = x1 + square_width, y1 + square_width

            cell_color = grid[row][column] # color
            cell_type = arrangement[row][column] # stored letter

            if cell_type == 'p':
                patch_1(100, x1, y1, window, cell_color)
                stored_objects[row][column] = 'p'
            elif cell_type == 'f':
                patch_2(18, 20, 5, 5, window, x1 + 10, y1, cell_color)
                stored_objects[row][column] = 'f'
            else:
                rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
                rectangle.fill_colour = cell_color
                rectangle.draw(window)
                stored_objects[row][column] = Rectangle


def clicked_point(window, arrangement, square_width, stored_objects):
    clicked_point = window.get_mouse()  # wait for person to click something

    if clicked_point:
        point_x, point_y = clicked_point.x, clicked_point.y

        cell_x = point_x // square_width  # identify the cells
        cell_y = point_y // square_width

        outline = Rectangle(Point(cell_x * square_width, cell_y * square_width),
                            Point(square_width* cell_x + square_width ,square_width* cell_y+ square_width))
        outline.outline_width = 4
        outline.draw(window)

        if 0 <= cell_x < len(arrangement[0]) and 0 <= cell_y < len(arrangement):
            chosen_cell = stored_objects[cell_y][cell_x]

            if isinstance(chosen_cell, Rectangle):
                chosen_cell.undraw()
                stored_objects[cell_y][cell_x] = None


if __name__ == "__main__":
    #import the stuff
    relative_size, grid_size = size()
    chosen_colors = colors()
    arrangement_grid = patch_grid(grid_size)
    colors = create_grid(chosen_colors, grid_size)
    stored_objects = [[None for _  in range(grid_size)] for _ in range (grid_size)]

    window = Window("Grid thingy", relative_size, relative_size)
    draw(window, colors, relative_size // grid_size,arrangement_grid, stored_objects)
    while True:
        clicked_point(window, arrangement_grid, relative_size// grid_size, stored_objects)