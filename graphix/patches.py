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


patch_2(50, 50, 5, 5, start_x=100, start_y=100)


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

