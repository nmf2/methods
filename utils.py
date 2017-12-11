#!/usr/bin/python2
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

"""
    Gets order of Adams-Moulton and Adams-Bashforth methods
"""
def getOrder():

        order = 1
        while True:
                try:
                    order = int(input("\nPlease input the degree of the method: "))
                    if order > 0:
                        break
                    else:
                        print "Degree must be greater than 0."
                except:
                    print "Please try again, invalid input."
        return order

def plot(mts, mys, labels, title):
    """
        mts = Array of arrays of t coordinates
        mys = Array of arrays of y coordinates
        labels = labels for each function. (i.e. points mts[0], mys[0] have the label labels[0])
        title = plot titlte
    """
    for i in range(len(mts)):
        plt.plot(mts[i], mys[i], label=labels[i])

    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title(title)

    plt.ticklabel_format(style='plain')              # disables scientific notation
    plt.legend(loc='best')                          # puts legend in the best place
    plt.show()


def runSimpleMethod(method, name):
    f = getFunction()

    t, y = getPoint(0)

    h, n = getNandH()

    ts, ys = method(f, t, y, h, n)
    
    plot([ts], [ys], [''], name)

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
    
    plt.legend(loc='best')  
    plt.ticklabel_format(style='plain')              # disables scientific notation
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
        
    points, ts, ys = adams_bashforth.method(f, p, h, n, order)

    plot([ts], [ys], [''], name)
    
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
    
    points, ts, ys = adams_moulton.method(f, p, h, n, order)

    plot([ts], [ys], [''], name)
    
    return ts, ys

def runAllMethods(order):
    f = getFunction()

    t, y = getPoint(0)

    h, n = getNandH()

    p = []          # array of points for adams methods

    ts1, ys1 = eulers.simple_euler(f, t, y, h, n)
    ts2, ys2 = eulers.improved_euler(f, t, y, h, n)
    ts3, ys3 = eulers.inverse_euler(f, t, y, h, n)
    ts4, ys4 = runge.method(f, t, y, h, n)

    if order == 1: order = 2                # makes sure at least one point is put into the p array
    for i in range(order):
        p.insert(0,Point2D(ts4[i], ys4[i])) # takes point generated from runge kutta method
        n = n - 1


    points, ts5, ys5 = adams_bashforth.method(f, p, h, n + 1, order)
    # p = []      #reset p
    # for i in range(order):
    #     p.insert(0,Point2D(ts4[i], ys4[i])) # takes point generated from runge kutta method
    p.pop()                                 # adams moulton takes order - 1 points to run
    points, ts6, ys6 = adams_moulton.method(f, p, h, n + 1, order)

    # 'points' is not necessary...
    
    #plot config
    plot(
        [ts1, ts2, ts3, ts4, ts5, ts6], 
        [ys1, ys2, ys3, ys4, ys5, ys6], 
        ['Simple Euler', 'Improved Euler', 'Inverse Euler', 'Runge-Kutta', 'Adams-Bashforth', 'Adams-Moulton'],
        'All Single Step methods'
        )

def allAdamsMoulton():
    mts = []
    mys = []
    pts = []
    p = []
    
    f = getFunction()

    t, y = getPoint(0)

    h, n = getNandH()

    ts, ys = runge.method(f, t, y, h, 7)
    p.insert(0,Point2D(ts[0], ys[0])) # takes point generated from runge kutta method
    for i in range(6):
        o = i + 1
        if i - 1 > 0: p.insert(0,Point2D(ts[i], ys[i])) # takes point generated from runge kutta method
        if i == 1:
            i = i -1
        pts, ts5, ys5 = adams_moulton.method(f, p, h, n-i, o)
        plot([ts5], [ys5], [''], 'Adams-Moulton of order {}'.format(o))
        os.system('clear')
        mts.append(ts5)
        mys.append(ys5)
        
    plot(
        mts, 
        mys, 
        ['1st Order', '2nd Order','3rd Order','4th Order','5th Order','6th Order'],
        'Adams-Moulton Methods (1-6)'
        )