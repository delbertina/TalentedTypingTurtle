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
        turtleletters.TurtleLetters.a()
    if letterList[0][i] == 'B':
        turtleletters.TurtleLetters.b()
    if letterList[0][i] == 'C':
        turtleletters.TurtleLetters.c()
    if letterList[0][i] == 'D':
        turtleletters.TurtleLetters.d()
    if letterList[0][i] == 'E':
        turtleletters.TurtleLetters.e()
    if letterList[0][i] == 'F':
        turtleletters.TurtleLetters.f()
    if letterList[0][i] == 'G':
        turtleletters.TurtleLetters.g()
    if letterList[0][i] == 'H':
        turtleletters.TurtleLetters.h()
    if letterList[0][i] == 'I':
        turtleletters.TurtleLetters.i()
    if letterList[0][i] == 'J':
        turtleletters.TurtleLetters.j()
    if letterList[0][i] == 'K':
        turtleletters.TurtleLetters.k()
    if letterList[0][i] == 'L':
        turtleletters.TurtleLetters.l()
    if letterList[0][i] == 'M':
        turtleletters.TurtleLetters.m()
    if letterList[0][i] == 'N':
        turtleletters.TurtleLetters.n()
    if letterList[0][i] == 'O':
        turtleletters.TurtleLetters.o()
    if letterList[0][i] == 'P':
        turtleletters.TurtleLetters.p()
    if letterList[0][i] == 'Q':
        turtleletters.TurtleLetters.q()
    if letterList[0][i] == 'R':
        turtleletters.TurtleLetters.r()
    if letterList[0][i] == 'S':
        turtleletters.TurtleLetters.s()
    if letterList[0][i] == 'T':
        turtleletters.TurtleLetters.t()
    if letterList[0][i] == 'U':
        turtleletters.TurtleLetters.u()
    if letterList[0][i] == 'V':
        turtleletters.TurtleLetters.v()
    if letterList[0][i] == 'W':
        turtleletters.TurtleLetters.w()
    if letterList[0][i] == 'X':
        turtleletters.TurtleLetters.x()
    if letterList[0][i] == 'Y':
        turtleletters.TurtleLetters.y()
    if letterList[0][i] == 'Z':
        turtleletters.TurtleLetters.z()
    if letterList[0][i] == ' ':
        turtle.forward(50)

    i += i
