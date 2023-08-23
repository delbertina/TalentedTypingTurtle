# set of lines that make a common set of lines

import turtle


# basic movements
def left_move(distance):
    turtle.left(90)
    turtle.forward(distance)


def right_move(distance):
    turtle.right(90)
    turtle.forward(distance)


def back_move(distance):
    turtle.right(180)
    turtle.forward(distance)


def left_move_double(distance1, distance2=None):
    left_move(distance1)
    if distance2 is None:
        left_move(distance1)
    else:
        left_move(distance2)


def right_move_double(distance1, distance2=None):
    right_move(distance1)
    if distance2 is None:
        right_move(distance1)
    else:
        right_move(distance2)


def left_right_move(distance1, distance2=None):
    left_move(distance1)
    if distance2 is None:
        right_move(distance1)
    else:
        right_move(distance2)


def right_left_move(distance1, distance2=None):
    right_move(distance1)
    if distance2 is None:
        left_move(distance1)
    else:
        left_move(distance2)

