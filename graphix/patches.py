from graphix import *


def patch_1(length, x, y, color):
    window = Window("Grid thingy", 500, 500)
    for i in range(0, length, 20):
        line1 = Line(Point(x, y + i), Point(i + x, y))
        line2 = Line(Point(x + i, y + length), Point(x + length, y + i))
        line3 = Line(Point(x, y + length - i), Point(x + i, y + length))
        line4 = Line(Point(x + i, y), Point(x + length, y + length - i))

        line1.draw(window), line2.draw(window), line3.draw(window), line4.draw(window)
        line1.fill_colour = color
        line1.outline_width = 2
        line2.fill_colour = color
        line2.outline_width = 2
        line3.fill_colour = color
        line3.outline_width = 2
        line4.fill_colour = color
        line4.outline_width = 2

patch_1(100, 100, 100, 'blue')



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
            triangle.fill_colour = color

            # Move to the next column
            x1_1 += base
            x2_1 += base
            x3_1 += base

        if row % 2 != 1:
            right_half = Polygon([Point(x1_1 - base // 2 - 80, start_y1),Point(x1_1- 80, start_y1),Point(x1_1 - base // 2 - 80, start_y1 + height)])
            right_half.draw(window)
            right_half.fill_colour = color

        # Handle the half-triangles at the ends of rows
        elif row % 2 != 0:  # Rows with offset need left and right half-triangles
            left_half = Polygon([Point(start_x1 + 70, start_y1),Point(70 + start_x1 + base // 2, start_y1 + height),Point(70 + start_x1 + base // 2, start_y1)])
            left_half.draw(window)
            left_half.fill_colour = color

        # Move to the next row
        start_y1 += height
        start_y2 += height
        start_y3 += height

    window = Window("Grid thingy", 100, 100)

    window.get_mouse()
    window.close()


    #patch_2(20, 20, 5, 4, start_x=100, start_y=100)

    color = 'red'

def patch_2(base, height, rows , cols, window, x ,y, color):
# fix the shapes eventually
    start_x1 , start_y1 = x , y
    start_x2 , start_y2 = x + base, y
    start_x3 , start_y3 = x + base // 2, y + height

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

        if row % 2 != 1:
            right_half = Polygon([Point(x1_1 - base // 2 - 100, start_y1),Point(x1_1- 100, start_y1),Point(x1_1 - base // 2 - 100, start_y1 + height)])
            right_half.draw(window)
            right_half.fill_colour = color

        # Handle the half-triangles at the ends of rows
        elif row % 2 != 0:  # Rows with offset need left and right half-triangles
            left_half = Polygon([Point(start_x1 + 90, start_y1),Point(90 + start_x1 + base // 2, start_y1 + height),Point(90 + start_x1 + base // 2, start_y1)])
            left_half.draw(window)
            left_half.fill_colour = color

        start_y1 += height
        start_y2 += height
        start_y3 += height


#patch_2(20, 20, 5, 5, window, 0, 0, color)

window.get_mouse()
window.close()

