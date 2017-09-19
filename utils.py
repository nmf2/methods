import sympy as sp
import os
import subprocess


def getFunction():
	while True:
		string = ''
		try:
			string = raw_input("Type in the f(t,y) function: ")  # get expression as string
			expr = sp.sympify(string)  # turn string expression into Sympy expression
			break
		except:
			print "Please try again, invalid input: {}", string
	
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


def plot(method):
	p = subprocess.Popen("cat implementations/{0}.conf | gnuplot".format(method), shell=True)
	os.waitpid(p.pid, 0)
	
	p = subprocess.Popen("xdg-open implementations/{0}.png".format(method), shell=True)
	os.waitpid(p.pid, 0)


def generateGnuPlotConf(pts, method):
	# write points to file:
	
	f = open('implementations/{0}_points.txt'.format(method), 'w')
	f.writelines(pts)
	f.close()
	
	# generate gnuplot configuration file:
	conf = '''\tset terminal png truecolor
			set output "implementations/{0}.png"
			set autoscale
			set style data lines
			plot "implementations/{0}_points.txt" using 1:2 title "{0}"'''.format(method)
	
	f = open('implementations/{0}.conf'.format(method), 'w')
	f.writelines(conf)
	f.close()

def runMethod(func, name):
	f = getFunction()
	
	t, y = getPoint(0)
	
	h, n = getNandH()
	
	points = func(f, t, y, h, n)
	
	generateGnuPlotConf(points, name)
	
	plot(name)
	
	print "Have a great day"
	
	return

from implementations import euler
runMethod(euler.euler, 'euler')