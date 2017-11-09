import sympy as sp
import os
import subprocess
from implementations import *

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


def plot(method):
	
	print "Running shell commands... might take a while.\n"
	
	p = subprocess.Popen("cat \"implementations/results/{0}.conf\" | gnuplot".format(method), shell=True)
	os.waitpid(p.pid, 0)

	p = subprocess.Popen("xdg-open \"implementations/results/{0}.png\"".format(method), shell=True)
	os.waitpid(p.pid, 0)
	
	print "Done!"


def generateGnuPlotConf(pts, method):
	
	# ensure directory exists
	
	directory = os.path.dirname('implementations/results/')
	if not os.path.exists(directory):
		os.makedirs(directory)

	# write points to file:
	f = open('implementations/results/{0}_points.txt'.format(method), 'w+')
	f.writelines(pts)
	f.close()
	
	# generate gnuplot configuration file:
	conf = '''\tset terminal png truecolor
			set output "implementations/results/{0}.png"
			set autoscale
			set style data lines
			plot "implementations/results/{0}_points.txt" using 1:2 title "{0}"'''.format(method)
	
	f = open('implementations/results/{0}.conf'.format(method), 'w')
	f.writelines(conf)
	f.close()

def runMethod(method, name):
	f = getFunction()

	t, y = getPoint(0)

	h, n = getNandH()

	points = method(f, t, y, h, n)
	
	generateGnuPlotConf(points, name)
	
	plot(name)

	print "\nHave a great day!"

	return

def runAllEulers():
	
	f = getFunction()

	t, y = getPoint(0)

	h, n = getNandH()

	points = eulers.euler(f, t, y, h, n)
	points1 = eulers.euler_enhanced(f, t, y, h, n)
	points2 = eulers.euler_inverted(f, t, y, h, n)

	generateGnuPlotConf(points, 'Euler')
	plot('Euler')
	generateGnuPlotConf(points1, "EulerEnhanced")
	plot("EulerEnhanced")
	generateGnuPlotConf(points2, "EulerInverted")
	plot("EulerInverted")

	print "\nHave a great day!"

	return

def runAdams(method, name, order):
	f = getFunction()
	
	p = []
	for i in range(order):
		p.insert(0,Point2D(getPoint(i)))
	
	h, n = getNandH()
	
	points = method(f, p, h, n, order)
	
	generateGnuPlotConf(points, name)
	plot(name)
	
	return
	
runAdams(adams_bashforth.method, 'Adams-bashforth', 6)