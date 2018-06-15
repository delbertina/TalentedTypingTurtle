# Taylor Cates
# set of lines that make a common set of lines

import turtle


class TurtleLines:
    letter = 'a'

    def __init__(self, letter):
        self.letter = letter

    @staticmethod
    def left_hundred():
        turtle.left(90)
        turtle.forward(100)

    @staticmethod
    def right_hundred():
        turtle.right(90)
        turtle.forward(100)

    @staticmethod
    def left_fifty():
        turtle.left(90)
        turtle.forward(50)

    @staticmethod
    def right_fifty():
        turtle.right(90)
        turtle.forward(50)

    @staticmethod
    def back_hundred():
        turtle.right(180)
        turtle.forward(100)

    @staticmethod
    def back_fifty():
        turtle.right(180)
        turtle.forward(50)

