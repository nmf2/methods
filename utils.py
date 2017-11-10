import sympy as sp
import os
import subprocess
from implementations import *
from matplotlib import pyplot as plt
from sympy import Point2D

def getFunction():
    while True:
        string = ''
        try:
            string = raw_input("Type in the f(t,y) function: ")  # get expression as string
            expr = sp.sympify(string)  # turn string expression into Sympy expression
            break
        except:
            print "Please try again, invalid input: ", string
    return expr


def getPoint(k):
    if k is None:  # in case the user doesn't want to specify which point they're getting
        k = ''
    while True:
        try:
            t = input("Type in t{0}: ".format(k))  # get k-th t as a number
            break
        except:
            print "Please try again, invalid input"
        
    while True:
        try:
            y = input("Type in y{0}: ".format(k))  # get k-th y as a number
            break
        except:
            print "Please try again, invalid input"
        
    return t, y


def getNandH():
    h = input("Type in the step h: ")  # gets h as number
    n = input("Type in the number of iterations n: ")  # gets h as number
        
    return h, n


def runSimpleMethod(method, name):
    f = getFunction()

    t, y = getPoint(0)

    h, n = getNandH()

    ts, ys = method(f, t, y, h, n)
    
    plt.plot(ts, ys)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(name)
    
    plt.show()

    print "\nHave a great day!"

    return ts, ys

def runAllEulers():
        
    f = getFunction()

    t, y = getPoint(0)

    h, n = getNandH()

    ts1, ys1 = eulers.simple_euler(f, t, y, h, n)
    ts2, ys2 = eulers.improved_euler(f, t, y, h, n)
    ts3, ys3 = eulers.inverse_euler(f, t, y, h, n)
    
    #plot config
    plt.plot(ts1, ys1, label='Simple Euler')
    plt.plot(ts2, ys2, label='Improved Euler')
    plt.plot(ts3, ys3, label='Inverse Euler')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title("All Euler Methods")
    
    #show plot
    plt.show()

    print "\nHave a great day!"

    return

def runAdamsBash(order):
    name = "Adams-Bashforth Method"
    f = getFunction()
        
    p = []
    for i in range(order):
        p.insert(0,Point2D(getPoint(i)))

    h, n = getNandH()
        
    points, ys, ts = adams_bashforth.method(f, p, h, n, order)

    plt.plot(ts, ys)

    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(name)

    plt.show()
    
    return ts, ys
def runAdamsMoulton(order):
    name = "Adams-Moulton Method"
    f = getFunction()
    p = []
    
    print '\nObs: Adams-Moulton of order k needs only k-1 points\n'
    
    
    if order == 1: order = 2                #makes sure at least one point is asked for
    for i in range(order - 1):
        p.insert(0,Point2D(getPoint(i)))

    h, n = getNandH()
    
    points, ys, ts = adams_moulton.method(f, p, h, n, order)

    plt.plot(ts, ys)
    
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(name)
    
    plt.show()
    
    return ts, ys