from sympy import Symbol
from sympy import solvers
from sympy import Eq



def moulton(f, p, h, n, order):
	print "Running Adams-Moulton of order {0}".format(order)
	
	points = []
	y = 0
	symbol_y = Symbol('y')
	
	for i in range(order):
		points = ["{0} {1}\n".format(p[i].x, p[i].y)]  # save point as a string with the following format: "t y\n"
	
	if order == 1:
		for i in range(n):
			p[0].x = p[0].x + h
			k1 = f.subs('t', p[0].x).subs('y', symbol_y)  # substitute t as a number and y as a symbol, this will return the expression f(tn+1, yn+1)
			
			result = solvers.solve(Eq(symbol_y, y + h * k1))  # this will solve the following equation yn+1 = yn + h*k1
			y = result[0]  # the previous method returns a list instead of a number, thus...
			
			points.append("{0} {1}\n".format(p[i].x, p[i].y))
		
		return points
	
	if order == 2:
		for i in range(n):
			[fk, p] = calc_fk(f, p, h)
			y = y + h * ((3 / 2) * fk[0] - (1 / 2) * fk[1])
			points.append("{0} {1}\n".format(p[i].x, p[i].y))
		return points
	
	if order == 3:
		for i in range(n):
			[fk, p] = calc_fk(f, p, h)
			y = y + h * ((23 / 12) * fk[0] - (4 / 3) * fk[1] + (5 / 12) * fk[2])
			points.append("{0} {1}\n".format(p[i].x, p[i].y))
		return points
	
	if order == 4:
		for i in range(n):
			[fk, p] = calc_fk(f, p, h)
			y = y + h * ((55 / 24) * fk[0] - (59 / 24) * fk[1] + (37 / 24) * fk[2] - (3 / 8) * fk[3])
			points.append("{0} {1}\n".format(p[i].x, p[i].y))
		return points
	
	if order == 5:
		for i in range(n):
			[fk, p] = calc_fk(f, p, h)
			y = y + h * (
				(1901 / 720) * fk[0] - (1387 / 360) * fk[1] + (109 / 30) * fk[2] - (637 / 360) * fk[3] + (251 / 720) * fk[4])
			points.append("{0} {1}\n".format(p[i].x, p[i].y))
		return points
	
	if order == 6:
		for i in range(n):
			[fk, p] = calc_fk(f, p, h)
			y = y + h * ((4277 / 1440) * fk[0] - (7923 / 1440) * fk[1] + (9982 / 1440) * fk[2] - (7298 / 1440) * fk[3] + (2877 / 1440) * fk[4] - (475 / 1440) * fk[5])
			points.append("{0} {1}\n".format(p[i].x, p[i].y))
		return points


def calc_fk(f, p, h):
	# Calculates: fn, fn-1... fn-j, doesn't calculate fn+1
	# the first
	fk = []
	i = 1                                               # doesn't start from 0 because fk[0] = fn+1
	for point in p:
		fk[i] = f.subs('t', p[i].x).subs('y', p[i].y)   # calculate each fk
		i = i + 1
	
	# fk[1] = fn, fk[2] = fn-1... fk[l] = fn-j
	
	
	return [fk, p]