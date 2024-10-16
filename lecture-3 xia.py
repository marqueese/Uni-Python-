import graphix
from graphix import Rectangle,Circle, Point, Line, Text, Window

def table():

    window = Window("the thing of shapes", 500, 500)

    r = Rectangle(Point(50, 100), Point(350, 300))
    r.outline_colour = "Black"
    r.outline_width = 5
    r.fill_colour = "Whitesmoke"
    r.draw(window)

    plate = Circle(Point(130, 160), 30)
    plate.fill_colour = "White"
    plate.outline_colour = "Black"
    plate.draw(window)
    window.mainloop()



def thing():

    window = graphix.Window("the funny thing of shapes", 500, 500)

    #the circles
    Circle_0 = Circle(Point(180, 160), 30)
    Circle_0.fill_colour = "black"
    Circle_0.outline_colour = "Black"
    Circle_0.draw(window)

    line_0 = Line(Point(210, 160), Point(330, 160))
    line_0.fill_colour = "black"
    line_0.outline_width = 4
    line_0.draw(window)

    Circle_1 = Circle(Point(330, 160), 30)
    Circle_1.fill_colour = "blue"
    Circle_1.outline_colour = "Black"
    Circle_1.draw(window)

    line_1 = Line(Point(352, 180), Point(420, 290))
    line_1.fill_colour = "black"
    line_1.outline_width = 4
    line_1.draw(window)

    Circle_2 = Circle(Point(420, 290), 30)
    Circle_2.fill_colour = "black"
    Circle_2.outline_colour = "Black"
    Circle_2.draw(window)

    line_2 = Line(Point(420, 290), Point(340, 390))
    line_2.fill_colour = "black"
    line_2.outline_width = 4
    line_2.draw(window)

    Circle_3 = Circle(Point(340, 390), 30)
    Circle_3.fill_colour = "blue"
    Circle_3.outline_colour = "Black"
    Circle_3.draw(window)

    point =Point(250, 250)
    message= "This is words"
    message = Text(point, message)

    message.draw(window)

    window.mainloop()



def other_thing():
    window = graphix.Window("the funny thing of shapes", 500, 500)

    point =Point(250, 250)
    #message= "This is words"
    #message = Text(point, message)

    input_text = input("put words here: ")
    text = "your words were " + input_text
    message = Text(point, text)
    message.draw(window)

    for i in range(10):
        window.get_mouse()
        message.move(0, -10)

    r = Rectangle(Point(50, 100), Point(350, 300))
    r.outline_colour = "Black"
    r.outline_width = 5
    r.draw(window)

    window.mainloop()

other_thing()