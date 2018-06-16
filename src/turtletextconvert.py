# Taylor Cates
# convert text to turtle drawing

import turtle
import turtleletters

# Get user input
letterInput = raw_input("Enter a letter: ")

# determine starting distance
if len(letterInput) > 1:
    gaps = len(letterInput) - 1
    letters = len(letterInput)
    startingDistance = -1 * (((gaps + letters) * 50) / 2)
else:
    startingDistance = -25

letterInput = letterInput.upper()
letterList = [letterInput]

i = 0

turtle.penup()
turtle.pensize(5)
turtle.goto(startingDistance, 0)

for i in range(len(letterInput)):
    if letterList[0][i] == 'A':
        turtleletters.a()
    if letterList[0][i] == 'B':
        turtleletters.b()
    if letterList[0][i] == 'C':
        turtleletters.c()
    if letterList[0][i] == 'D':
        turtleletters.d()
    if letterList[0][i] == 'E':
        turtleletters.e()
    if letterList[0][i] == 'F':
        turtleletters.f()
    if letterList[0][i] == 'G':
        turtleletters.g()
    if letterList[0][i] == 'H':
        turtleletters.h()
    if letterList[0][i] == 'I':
        turtleletters.i()
    if letterList[0][i] == 'J':
        turtleletters.j()
    if letterList[0][i] == 'K':
        turtleletters.k()
    if letterList[0][i] == 'L':
        turtleletters.l()
    if letterList[0][i] == 'M':
        turtleletters.m()
    if letterList[0][i] == 'N':
        turtleletters.n()
    if letterList[0][i] == 'O':
        turtleletters.o()
    if letterList[0][i] == 'P':
        turtleletters.p()
    if letterList[0][i] == 'Q':
        turtleletters.q()
    if letterList[0][i] == 'R':
        turtleletters.r()
    if letterList[0][i] == 'S':
        turtleletters.s()
    if letterList[0][i] == 'T':
        turtleletters.t()
    if letterList[0][i] == 'U':
        turtleletters.u()
    if letterList[0][i] == 'V':
        turtleletters.v()
    if letterList[0][i] == 'W':
        turtleletters.w()
    if letterList[0][i] == 'X':
        turtleletters.x()
    if letterList[0][i] == 'Y':
        turtleletters.y()
    if letterList[0][i] == 'Z':
        turtleletters.z()
    if letterList[0][i] == ' ':
        turtle.forward(50)

    i += i
