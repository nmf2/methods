from sympy import Symbol
from sympy import solvers
from sympy import Eq
def euler(f, t, y, h, n):
	
	print "Running Euler"
	points = ["{0} {1}\n".format(t, y)]  # save point as a string with the following format: "t y\n"
	
	for i in range(n):
		k1 = f.subs('t', t).subs('y', y)  # substitute t then y
		y = y + h * k1
		t = t + h
		
		points.append("{0} {1}\n".format(t, y))
	
	return points

def euler_method(f, t, y, h):
	
	k1 = f.subs('t', t).subs('y', y)  # substitute t then y
	y = y + h * k1
	
	return y


def euler_enhanced(f, t, y, h, n):
	#Euler Enhanced (Aprimorado)
	
	print "Running Euler Enhanced"
	points = ["{0} {1}\n".format(t, y)]             # save point as a string with the following format: "t y\n"
	
	for i in range(n):
		k1 = f.subs('t', t).subs('y', y)            # substitute t then y
		k2 = f.subs('t', t+h).subs('y',y + h*k1)
		y = y + (h/2)*(k1 + k2)
		t = t + h
		
		points.append("{0} {1}\n".format(t, y))
	
	return points


def euler_inverted(f, t, y, h, n):
	# Euler Inverted (Inverso)
	points = ["{0} {1}\n".format(t, y)]             # save point as a string with the following format: "t y\n"
	print "Running Euler Inverted"
	symbol_y = Symbol('y')
	
	for i in range(n):
		t = t + h
		k1 = f.subs('t', t).subs('y', symbol_y)             # substitute t as a number and y as a symbol, this will return the expression f(tn+1, yn+1)
		result = solvers.solve(Eq(symbol_y, y + h * k1))    # this will solve the following equation yn+1 = yn + h*k1
		y = result[0]                                       # the previous method returns a list instead of a number, thus...
		
		points.append("{0} {1}\n".format(t, y))
	
	return points
