from graphix import *

def patch_2(base, height, rows , cols):
    window = Window("small grid", 500, 500)

    start_x1 , start_y1 = 0, 0
    start_x2 , start_y2 = base, 0
    start_x3 , start_y3 = base // 2, height

    for row in range(rows):
        offset = -(base // 2) if row % 2 != 0 else 0 # if the row number has no remainders shift it by the base

        x1_1, x2_1, x3_1 = start_x1 + offset, start_x2 + offset, start_x3 + offset

        for column in range(cols):

            x1 = Point(x1_1, start_y1)
            x2 = Point(x2_1, start_y2)
            x3 = Point(x3_1, start_y3)

            triangle = Polygon([x1, x2, x3])
            triangle.draw(window)
            triangle.fill_colour = "red"

            x1_1 += base
            x2_1 += base
            x3_1 += base

        start_y1 += height
        start_y2 += height
        start_y3 += height

    window.get_mouse()
    window.close()

patch_2(25, 30, 15, 16)


def patch_1(length):

    window = Window("small grid", 500, 500)

    for i in range(0, length, 20):
        line1 = Line(Point(0, i), Point(i, 0))
        line1.draw(window)
        line1.fill_colour = "blue"

        line2 = Line(Point(i, 100), Point(100, i))
        line2.draw(window)
        line2.fill_colour = "red"

    for i in range(0, length, 20):
        line3 = Line(Point(0, 100 - i), Point(i, 100))
        line3.draw(window)
        line3.fill_colour = "blue"

        line4 = Line(Point(i, 0), Point(100, 100 - i))
        line4.draw(window)
        line4.fill_colour = "red"

    window.get_mouse()
    window.close()

#patch_1(100)