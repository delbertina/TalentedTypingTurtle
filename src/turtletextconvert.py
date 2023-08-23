# convert text to turtle drawing

import turtle
import turtleletters
import math


def calc_start(letter_input):
    if len(letter_input) > 1:
        gaps = len(letter_input) - 1
        letters = len(letter_input)
        starting_distance = -1 * (((gaps + letters) * 50) / 2)
        if abs(starting_distance) > (turtle.window_width() / 2):
            starting_distance = 0 - ((turtle.window_width / 2) - 25)
    else:
        starting_distance = -25
    print "Starting distance: " + str(starting_distance)
    return starting_distance


def text_wrap_draw(letter_input):
    starting_distance = -25

# if can fit on one line
    if len(letter_input) > 1 & (((len(letter_input) - 1) * 25) > (turtle.window_width / 2)):
        starting_distance = -1 * ((len(letter_input) - 1) * 25)
# if cannot fit on one line
    else:
        line_capacity = math.floor((turtle.window_width() / 100))


def draw_text(letter_input, starting_distance):
    letter_upper = letter_input.upper()
    letter_list = [letter_upper]

    turtle.penup()
    turtle.pensize(5)
    turtle.goto(starting_distance, 0)

    for i in range(len(letter_upper)):
        if letter_list[0][i] == 'A':
            turtleletters.a()
        if letter_list[0][i] == 'B':
            turtleletters.b()
        if letter_list[0][i] == 'C':
            turtleletters.c()
        if letter_list[0][i] == 'D':
            turtleletters.d()
        if letter_list[0][i] == 'E':
            turtleletters.e()
        if letter_list[0][i] == 'F':
            turtleletters.f()
        if letter_list[0][i] == 'G':
            turtleletters.g()
        if letter_list[0][i] == 'H':
            turtleletters.h()
        if letter_list[0][i] == 'I':
            turtleletters.i()
        if letter_list[0][i] == 'J':
            turtleletters.j()
        if letter_list[0][i] == 'K':
            turtleletters.k()
        if letter_list[0][i] == 'L':
            turtleletters.l()
        if letter_list[0][i] == 'M':
            turtleletters.m()
        if letter_list[0][i] == 'N':
            turtleletters.n()
        if letter_list[0][i] == 'O':
            turtleletters.o()
        if letter_list[0][i] == 'P':
            turtleletters.p()
        if letter_list[0][i] == 'Q':
            turtleletters.q()
        if letter_list[0][i] == 'R':
            turtleletters.r()
        if letter_list[0][i] == 'S':
            turtleletters.s()
        if letter_list[0][i] == 'T':
            turtleletters.t()
        if letter_list[0][i] == 'U':
            turtleletters.u()
        if letter_list[0][i] == 'V':
            turtleletters.v()
        if letter_list[0][i] == 'W':
            turtleletters.w()
        if letter_list[0][i] == 'X':
            turtleletters.x()
        if letter_list[0][i] == 'Y':
            turtleletters.y()
        if letter_list[0][i] == 'Z':
            turtleletters.z()
        if letter_list[0][i] == ' ':
            turtle.forward(50)

        i += i


# Get user input
letterInput = raw_input("Enter text to draw: ")

print str(turtle.window_width())

# determine starting distance
startingDistance = calc_start(letterInput)

draw_text(letterInput, startingDistance)
turtle.exitonclick()

