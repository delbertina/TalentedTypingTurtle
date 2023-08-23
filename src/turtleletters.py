# Set of lines that make up each letter

import turtle
import turtlelines


def a():
    turtle.pendown()
    turtlelines.left_right_move(100, 50)
    turtlelines.right_move_double(40, 50)
    turtlelines.back_move(50)
    turtlelines.right_move(60)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)


def b():
    turtle.pendown()
    turtlelines.left_right_move(100, 40)
    turtlelines.right_move_double(50, 40)
    turtlelines.back_move(50)
    turtlelines.right_move_double(50)
    turtlelines.back_move(50)
    turtle.penup()
    turtle.forward(50)


def c():
    turtle.pendown()
    turtle.forward(50)
    turtlelines.back_move(50)
    turtlelines.right_move_double(100, 50)
    turtle.penup()
    turtlelines.right_left_move(100, 50)


def d():
    turtle.pendown()
    turtle.forward(40)
    turtlelines.back_move(40)
    turtlelines.right_move_double(100, 40)
    turtlelines.right_left_move(10)
    turtlelines.right_move_double(80, 10)
    turtlelines.left_move(10)
    turtle.penup()
    turtlelines.left_move(50)


def e():
    turtle.pendown()
    turtle.forward(50)
    turtlelines.back_move(50)
    turtlelines.right_move_double(50, 30)
    turtlelines.back_move(30)
    turtlelines.right_move_double(50)
    turtle.penup()
    turtlelines.right_left_move(100, 50)


def f():
    turtle.pendown()
    turtlelines.left_right_move(50, 30)
    turtlelines.back_move(30)
    turtlelines.right_move_double(50)
    turtle.penup()
    turtlelines.right_left_move(100, 50)


def g():
    turtle.pendown()
    turtle.forward(50)
    turtlelines.left_move_double(40, 20)
    turtle.penup()
    turtlelines.left_right_move(40, 30)
    turtle.pendown()
    turtlelines.right_move_double(100, 50)
    turtle.penup()
    turtlelines.right_left_move(100, 50)


def h():
    turtle.pendown()
    turtlelines.left_move(100)
    turtlelines.back_move(50)
    turtlelines.left_move_double(50)
    turtlelines.back_move(100)
    turtle.penup()
    turtlelines.left_move(50)


def i():
    turtle.pendown()
    turtle.forward(50)
    turtlelines.back_move(25)
    turtlelines.right_left_move(100, 25)
    turtlelines.back_move(50)
    turtle.penup()
    turtlelines.right_left_move(100, 50)


def j():
    turtlelines.left_move(20)
    turtle.pendown()
    turtlelines.back_move(20)
    turtlelines.left_move_double(30, 100)
    turtlelines.left_move(30)
    turtlelines.back_move(50)
    turtle.penup()
    turtlelines.right_left_move(100, 50)


def k():
    turtle.pendown()
    turtlelines.left_move(100)
    turtlelines.back_move(50)
    turtlelines.left_move_double(30, 10)
    turtlelines.right_left_move(10)
    turtlelines.right_left_move(10, 30)
    turtle.penup()
    turtlelines.left_move_double(50)
    turtlelines.left_move(30)
    turtle.pendown()
    turtlelines.right_left_move(10)
    turtlelines.right_left_move(20, 10)
    turtlelines.right_move(20)
    turtle.penup()
    turtlelines.left_move(50)


def l():
    turtle.pendown()
    turtlelines.left_move(100)
    turtlelines.back_move(100)
    turtlelines.left_move(50)
    turtle.penup()
    turtle.forward(50)


def m():
    turtle.pendown()
    turtlelines.left_right_move(100, 10)
    turtlelines.right_left_move(20, 10)
    turtlelines.right_left_move(20, 10)
    turtlelines.left_right_move(20, 10)
    turtlelines.left_right_move(20, 10)
    turtlelines.right_move(100)
    turtle.penup()
    turtlelines.left_move(50)


def n():
    turtle.pendown()
    turtlelines.left_right_move(100, 10)
    turtlelines.right_left_move(20, 10)
    turtlelines.right_left_move(20, 10)
    turtlelines.right_left_move(40, 10)
    turtlelines.right_left_move(20, 10)
    turtlelines.left_move(100)
    turtle.penup()
    turtlelines.back_move(100)
    turtlelines.left_move(50)


def o():
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(30)
    turtlelines.left_right_move(10)
    turtlelines.left_move_double(80, 10)
    turtlelines.right_left_move(10, 30)
    turtlelines.left_right_move(10)
    turtlelines.left_move_double(80, 10)
    turtlelines.right_move(10)
    turtle.penup()
    turtlelines.left_move(90)


def p():
    turtle.pendown()
    turtlelines.left_right_move(100, 40)
    turtlelines.right_left_move(10)
    turtlelines.right_move_double(30, 10)
    turtlelines.left_right_move(10, 40)
    turtle.penup()
    turtlelines.left_move_double(50, 100)


def q():
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(30)
    turtlelines.left_right_move(10)
    turtlelines.left_move_double(80, 10)
    turtlelines.right_left_move(10, 30)
    turtlelines.left_right_move(10)
    turtlelines.left_move_double(80, 10)
    turtlelines.right_left_move(10, 20)
    turtlelines.left_move(15)
    turtlelines.back_move(15)
    turtlelines.left_move(20)
    turtle.penup()
    turtle.forward(50)


def r():
    turtle.pendown()
    turtlelines.left_right_move(100, 40)
    turtlelines.right_left_move(10)
    turtlelines.right_move_double(30, 10)
    turtlelines.left_right_move(10, 40)
    turtlelines.back_move(30)
    turtlelines.right_left_move(10)
    turtlelines.right_left_move(20, 10)
    turtlelines.right_move(20)
    turtle.penup()
    turtlelines.left_move(50)


def s():
    turtle.pendown()
    turtle.forward(40)
    turtlelines.left_right_move(10)
    turtlelines.left_move_double(30, 10)
    turtlelines.right_left_move(10, 30)
    turtlelines.right_left_move(10)
    turtlelines.right_move_double(30, 10)
    turtlelines.left_right_move(10, 40)
    turtle.penup()
    turtlelines.right_left_move(100, 50)


def t():
    turtle.forward(25)
    turtle.pendown()
    turtlelines.left_move_double(100, 25)
    turtlelines.back_move(50)
    turtle.penup()
    turtlelines.right_left_move(100, 50)


def u():
    turtlelines.left_move(100)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(90)
    turtlelines.left_right_move(10)
    turtlelines.left_move_double(30, 10)
    turtlelines.right_left_move(10, 90)
    turtle.penup()
    turtlelines.back_move(100)
    turtlelines.left_move(50)


def v():
    turtlelines.left_move(100)
    turtle.pendown()
    turtlelines.back_move(40)
    turtlelines.left_right_move(10, 40)
    turtlelines.left_right_move(10, 20)
    turtlelines.left_move_double(10, 20)
    turtlelines.right_left_move(10, 40)
    turtlelines.right_left_move(10, 40)
    turtle.penup()
    turtlelines.back_move(100)
    turtlelines.left_move(50)


def w():
    turtlelines.left_move(100)
    turtle.pendown()
    turtlelines.back_move(50)
    turtlelines.left_right_move(10, 50)
    turtlelines.left_move_double(10, 40)
    turtlelines.right_move_double(10, 40)
    turtlelines.left_move_double(10, 50)
    turtlelines.right_left_move(10, 50)
    turtle.penup()
    turtlelines.back_move(100)
    turtlelines.left_move(50)


def x():
    turtle.pendown()
    turtlelines.left_right_move(20, 10)
    turtlelines.left_right_move(20, 10)
    turtlelines.left_right_move(10)
    turtlelines.left_right_move(10)
    turtlelines.left_right_move(20, 10)
    turtlelines.left_move(20)
    turtle.penup()
    turtlelines.left_move(50)
    turtle.pendown()
    turtlelines.left_move_double(20, 10)
    turtlelines.right_left_move(20, 10)
    turtlelines.right_left_move(10)
    turtlelines.right_left_move(10)
    turtlelines.right_left_move(20, 10)
    turtlelines.right_move(20)
    turtle.penup()
    turtlelines.left_move(50)


def y():
    turtle.forward(20)
    turtlelines.left_move(50)
    turtle.pendown()
    turtlelines.right_left_move(10)
    turtlelines.right_left_move(10, 20)
    turtlelines.right_left_move(10, 20)
    turtle.penup()
    turtlelines.left_move(50)
    turtle.pendown()
    turtlelines.left_move_double(20, 10)
    turtlelines.right_left_move(20, 10)
    turtlelines.right_left_move(10, 5)
    turtlelines.right_move(50)
    turtle.penup()
    turtlelines.left_move(75)


def z():
    turtle.pendown()
    turtlelines.left_right_move(20, 10)
    turtlelines.left_right_move(20, 10)
    turtlelines.left_right_move(10)
    turtlelines.left_right_move(10)
    turtlelines.left_right_move(20, 10)
    turtlelines.left_move_double(20, 50)
    turtle.penup()
    turtlelines.left_move(100)
    turtle.pendown()
    turtlelines.left_move(50)
    turtle.penup()
    turtle.forward(50)
