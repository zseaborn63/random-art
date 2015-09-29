import random
import math
import cmath

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def quadrants(x, y):
    w = math.atan(math.pi ** 6 * (x * y) * 90)
    return w
    # this one makes quadrants

def simple(x, y):
    h = x + y
    return h

def sonar_waves(x, y):
    it_might_be = math.tan((math.pi * math.sin(x) - math.cos(y))) + math.atan((math.pi * math.cos(y) - math.sin(x)))
    return it_might_be
    # this one gives you a double curve facing the same way

def x_shape(x, y):
    func = [math.sin, math.cos, math.tan]
    h = math.atan(math.pi * math.tan(x -y) * x) - math.tan(math.pi * math.atan(y - x) * y)
    return h
    # this returns a crazy fractile-like shape that's almost like an X

def corner_curves(x, y):
    w = math.sin(math.sin(math.pi*math.cos(x + y)) + math.tan(math.pi*math.atan(x * y)))
    return w
    # this one returns curves at the four corners

def crazy(x, y):
    c = math.tan(math.sin(math.pi * x * math.cos(y))) + math.tan(math.sin(math.pi * y * math.cos(x)))
    return c

def shaper(x, y):
    rr = math.tan((x**3 + y**3)*math.pi)
    return rr
    # this one returns shapes that change depending on the exponent

def me(x, y):
    ggh = math.tan(math.atan(x**2 - y**2)*math.pi)
    return ggh

def funky_cold_medina(x, y):
    fcm = math.tan(math.sin(abs(x) ** 0.5 *math.cos(x ** 10 + math.tan(x**2 - y**2)))) + math.tan(math.pi) * math.sin(abs(y) ** 0.5 * math.cos(math.tan(y**2 - x**2)))
    return fcm

def b_sym(x, y):
    b = math.tan((x * y) **2) * math.pi + math.cos((x * y)**2) * math.pi + math.cos((x * y)**2) * math.pi + math.atan((x * y)**2) * math.pi
    return b

def multi_lines(x, y):
    nn = math.tan(math.e * (x**2 + y**8))
    return nn
    # this will make crazy shapes depending on the exponents

def idk(x, y):
    hhj = math.tan(x * math.e) + math.sin((x + y) * math.e) + math.cos(y * math.e)
    return hhj

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    expr = random.choice([multi_lines, corner_curves, idk])
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
