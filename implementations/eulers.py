from sympy import Symbol
from sympy import solvers
from sympy import Eq

def simple_euler(f, t, y, h, n):
	#Simple Euler
	
	print "Running Simple Euler Method"
	ts = [t]
	ys = [y]
	
	for i in range(n):
		k1 = f.subs('t', t).subs('y', y)  # substitute t then y
		y = y + h * k1
		t = t + h
		
		ts.append(t)
		ys.append(y)
	
	return ts, ys

def improved_euler(f, t, y, h, n):
	print "Running Improved Euler Method"
	ts = [t]
	ys = [y]
	
	for i in range(n):
		k1 = f.subs('t', t).subs('y', y)            # substitute t then y
		k2 = f.subs('t', t+h).subs('y',y + h*k1)
		y = y + (h/2)*(k1 + k2)
		t = t + h
		
		ts.append(t)
		ys.append(y)
	
	return ts, ys


def inverse_euler(f, t, y, h, n):
	ts = [t]
	ys = [y]
	
	print "Running Inverse Euler Method"
	symbol_y = Symbol('y')                          # yn+1
	
	for i in range(n):
		t = t + h
		k1 = f.subs('t', t).subs('y', symbol_y)             # substitute t as a number and y as a symbol, this will return the expression f(tn+1, yn+1)
		result = solvers.solve(Eq(symbol_y, y + h * k1))    # this will solve the following equation yn+1 = yn + h*k1
		y = result[0]                                       # the previous method returns a list instead of a number, thus...
		
		ts.append(t)
		ys.append(y)
	
	return ts, ys
