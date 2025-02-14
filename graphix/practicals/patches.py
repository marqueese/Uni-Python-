from graphix import *

window = Window("Grid thingy", 500, 500)

def patch_2(base, height, rows, cols, start_x=0, start_y=0):#
    start_x1, start_y1 = start_x, start_y
    start_x2, start_y2 = start_x + base, start_y
    start_x3, start_y3 = start_x + base // 2, start_y + height

    for row in range(rows):
        offset = -(base // 2) if row % 2 != 0 else 0  # Offset for alternate rows

        x1_1, x2_1, x3_1 = start_x1 + offset, start_x2 + offset, start_x3 + offset

        for column in range(cols):
            # Draw the full triangle
            x1 = Point(x1_1, start_y1)
            x2 = Point(x2_1, start_y2)
            x3 = Point(x3_1, start_y3)

            triangle = Polygon([x1, x2, x3])
            triangle.draw(window)
            triangle.fill_colour = "red"

            # Move to the next column
            x1_1 += base
            x2_1 += base
            x3_1 += base

        # Handle the half-triangles at the ends of rows
        if row % 2 != 0:  # Rows with offset need left and right half-triangles
            left_half = Polygon([Point(start_x1, start_y1),
                                 Point(start_x1 + base // 2, start_y1 + height),
                                 Point(start_x1 + base // 2, start_y1)])
            left_half.draw(window)
            left_half.fill_colour = "red"

            right_half = Polygon([Point(x1_1 - base // 2, start_y1),
                                  Point(x1_1, start_y1),
                                  Point(x1_1 - base // 2, start_y1 + height)])
            right_half.draw(window)
            right_half.fill_colour = "red"

        # Move to the next row
        start_y1 += height
        start_y2 += height
        start_y3 += height

    window.get_mouse()
    window.close()

#patch_2(50, 50, 5, 5, start_x=100, start_y=100)

def patch_1(length, x, y ):

    window = Window("small grid", 500, 500)

    for i in range(0, length, 20):
        line1 = Line(Point(x,y + i), Point(i + x, y))
        line1.draw(window)
        line1.fill_colour = "blue"

        line2 = Line(Point(x+ i, y + 100), Point(x + 100, y+ i))
        line2.draw(window)
        line2.fill_colour = "red"

    for i in range(0, length, 20):
        line3 = Line(Point(x,y + 100 - i), Point(x+ i, y+ 100))
        line3.draw(window)
        line3.fill_colour = "blue"

        line4 = Line(Point(x+ i, y), Point(x+ 100, y+ 100 - i))
        line4.draw(window)
        line4.fill_colour = "red"

    window.get_mouse()
    window.close()

#patch_1(100, 50, 50)

key = window.get_key()
print(key)

if key == "x":
    window.close()
else:
    print("shits busted")

#didnt work
if __name__ == "__main__":
    #import the stuff.py
    relative_size, grid_size = size()
    chosen_colors = colors()
    arrangement_grid = patch_grid(grid_size)
    grid  = create_grid(chosen_colors, grid_size)

    window = Window("Grid thingy", relative_size, relative_size)
    stored_objects = [[None for _ in range(grid_size)] for _ in range(grid_size)] # hate this thing
    draw(window, grid, relative_size // grid_size,arrangement_grid, stored_objects)

    click_state = {"processing": False, "outline": None, "previous_patch": None}

    while True:
        result = click_outline(window, relative_size // grid_size)

        keyboard_select(window, relative_size // grid_size)


def delete_patch(window, square_width,click_state):
    result = click_outline(window, square_width)

    if not result or click_state["processing"]:
        return

    cell_y , cell_x = result

    if click_state["previous_patch"] is not None:
       patch = click_state["previous_patch"]
       if isinstance(patch, list):
           for item in patch:
               item.undraw()
       else:
            patch.undraw()

    current_patch = stored_objects[cell_y][cell_x]

        if current_patch is not None:
           if isinstance(current_patch, list):
               for item in current_patch:
                    item.undraw()
           else:
                current_patch.undraw()

def click_outline(window , square_width):
    if click_state["processing"]:
        return

    click_state["processing"] = True
    clicked = window.get_mouse()  # wait for person to click something

    if clicked:
        point_x, point_y = clicked.x, clicked.y
        cell_x = point_x // square_width  # identify the cells
        cell_y = point_y // square_width

        if click_state["outline"]:
            click_state["outline"].undraw()

        outline = Rectangle(Point(cell_x * square_width, cell_y * square_width),Point(square_width * cell_x + square_width, square_width * cell_y + square_width))
        outline.outline_width = 4
        outline.draw(window)

        click_state["outline"] = outline
        click_state["processing"] = False
        return cell_y, cell_x
    click_state["processing"] = False
    return None

