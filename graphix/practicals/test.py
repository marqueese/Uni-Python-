from graphix import *


def clicking():
    window = Window("Graph", 500, 500)

    # Get the initial click location for the text position
    click_x, click_y = window.get_mouse()  # Initial click coordinates
    i = 1

    # Create the first text object at the clicked position
    message = "H" + "i" * i
    text = Text((click_x, click_y), message)
    text.draw(window)

    # Update the text each time a click occurs
    for _ in range(9):  # Repeat 9 more times to reach 10 clicks
        i += 1
        message = "H" + "i" * i

        # Undraw the previous text and create a new one at the same coordinates
        text.undraw()
        text = Text((click_x, click_y), message)
        text.draw(window)

        window.get_mouse()  # Wait for the next click

    window.get_mouse()  # Wait for a final click to close
    window.close()


clicking()