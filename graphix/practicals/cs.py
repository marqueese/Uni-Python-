from graphix import Line, Point, Polygon, Rectangle, Window

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

    color_list = {
            '1':'red', '2': 'green', '3': 'blue' ,'4': 'orange', '5': 'purple', '6': 'magenta'
        }

    while len(chosen_color) < 3: # runs until 3 colors are chosen
        color_choice  = input("Pick a color you want: ")

        if not color_choice.isdigit() or color_choice not in color_list:
            print("Enter a number from 1-6")
            continue

        if color_choice < '1' or color_choice > '6':
            print("Enter a number from the list provided")
            continue

        color_name = color_list[color_choice]

        if color_name in chosen_color:
            print("You have already chosen this color")
        else:
            chosen_color.append(color_name) # set a variable for the color to add
    return chosen_color #colors should be stored in this


def patch_1(length, x, y, window, color):
    shape = []

    def draw_line(x1, y1, x2, y2):
        line = Line(Point(x1, y1),Point(x2, y2))
        line.draw(window)
        line.outline_colour = color
        line.outline_width = 2
        shape.append(line)

    for i in range(0, length, 20):
        draw_line(x , y + i, i + x, y)
        draw_line(x+ i, y + length ,x + length, y+ i)
        draw_line(x, y + length - i, x + i, y + length)
        draw_line(x + i, y, x + length, y + length - i)
    return shape


def patch_2(base, height, rows , cols, window, x ,y, color):
    shape = []
    start_x1 , start_y1 = x , y
    start_x2 , start_y2 = x + base, y
    start_x3 , start_y3 = x + base // 2, y + height

    def draw_triangles(x1, y1, x2, y2, x3, y3):
        points = [Point(x1, y1), Point(x2, y2), Point(x3, y3)] #assign points
        triangle = Polygon(points)
        triangle.draw(window)
        triangle.fill_colour = color
        shape.append(triangle)

    def draw_half_triangle(x1, y1, x2, y2, x3, y3):
        points = [Point(x1, y1), Point(x2, y2), Point(x3, y3)]  # assign points
        half_triangle = Polygon(points)
        half_triangle.draw(window)
        half_triangle.fill_colour = color
        shape.append(half_triangle)

    for row in range(rows):
        offset = -(base // 2) if row % 2 != 0 else 0 # if the row number has no remainders shift it by the base
        x1_1, x2_1, x3_1 = start_x1 + offset, start_x2 + offset, start_x3 + offset

        for column in range(cols):
            draw_triangles(x1_1, start_y1, x2_1, start_y2, x3_1, start_y3)
            x1_1, x2_1 , x3_1 = x1_1 +  base, x2_1 + base , x3_1 + base

        if row % 2 != 1:
            draw_half_triangle(x1_1 - base // 2 - 90, start_y1, x1_1- 90, start_y1 ,x1_1 - base // 2 - 90, start_y1 + height)
        elif row % 2 != 0:
            draw_half_triangle(start_x1 + 80, start_y1, 80 + start_x1 + base // 2, start_y1 + height, 80 + start_x1 + base // 2, start_y1)

        start_y1, start_y2, start_y3 = start_y1 + height, start_y2 + height, start_y3 + height
    return shape


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


def draw(window, grid, square_width, arrangement, stored_objects): # call this one to make stuff.py
    rows, columns = len(grid), len(grid[0])# specify this when making the graph thingy
    for row in range(rows):
        for column in range (columns):
            x1, y1 = column * square_width, row * square_width
            x2, y2 = x1 + square_width, y1 + square_width

            cell_color = grid[row][column] # color
            cell_type = arrangement[row][column] # stored letter

            if cell_type == 'p':
                stored_objects[row][column] = patch_1(100, x1, y1, window, cell_color)
            elif cell_type == 'f':
                stored_objects[row][column] = patch_2(18, 20, 5, 5, window, x1 + 10, y1, cell_color)
            else:
                rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
                rectangle.fill_colour = cell_color
                rectangle.draw(window)
                stored_objects[row][column] = rectangle


def click_outline(window, square_width, state):
    if state["processing"]:
        return None, None

    state["processing"] = True
    clicked = window.get_mouse()  # wait for person to click something

    if clicked is not None:
        point_x = clicked.x
        point_y = clicked.y

        cell_x = point_x // square_width  # identify the cells
        cell_y = point_y // square_width

        if state["outline"]:
            state["outline"].undraw()

        outline = Rectangle(Point(cell_x * square_width, cell_y * square_width),Point(square_width * cell_x + square_width, square_width * cell_y + square_width))
        outline.outline_width = 4
        outline.draw(window)

        state["outline"] = outline
        state["processing"] = False
        return point_x, point_y
    state["processing"] = False
    return None, None


def delete_patch(window, square_width, state, x, y):
    click_state["processing"] = True # set to true should stop any new inpiuts

    cell_x = x // square_width
    cell_y = y // square_width

    if state["previous_patch"]:
        patch = state["previous_patch"]
        if isinstance(patch, list): #is the data type a list if not its a rectangle
            for item in patch:
                item.undraw()
        else:
            patch.undraw()
        click_state["outline"].undraw()


    current_patch = stored_objects[cell_y][cell_x]
    if current_patch:
        if isinstance(current_patch, list):
            for item in current_patch:
                item.undraw()
        else:
            current_patch.undraw()
        click_state["outline"].undraw()


def keyboard_inputs(window, square_width, x , y):
    print("x: delete patch\nesc: deselect patch")

    while True:
        chosen_key = window.get_key()

        if chosen_key.lower() == "x":
            delete_patch(window, square_width, click_state, x, y)
            print("patch deleting")
            break
        elif chosen_key.lower() == "esc":
            print("unselecting patch") # no idea if thats even a word
            break
        else:
             break

if __name__ == "__main__":
    #import the stuff
    relative_size, grid_size = size()
    chosen_colors = colors()
    arrangement_grid = patch_grid(grid_size)
    grid  = create_grid(chosen_colors, grid_size)
    window = Window("Grid thingy", relative_size, relative_size)
    click_state = {"processing": False, "outline": None, "previous_patch": None}

    stored_objects = [[None for _ in range(grid_size)] for _ in range(grid_size)]

    draw(window, grid, relative_size // grid_size,arrangement_grid, stored_objects)

    while True:
        x, y = click_outline(window, relative_size // grid_size, click_state)

        if x is not None and y is not None:
            keyboard_inputs(window, relative_size // grid_size, x, y)
            print("you returned")

        click_state["processing"] = False