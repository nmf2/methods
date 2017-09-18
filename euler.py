import sympy as sp
import os
import subprocess


def euler(f, t, y, h, n):
	points = ["{0} {1}\n".format(t, y)]		     # save point as a string with the following format: "t y\n"

	for i in range(n):

		k1 = f.subs('y', y).subs('t', t)		    # substitute y then t
		y = y + h*k1
		t = t + h

		points.append("{0} {1}\n".format(t, y))

	return points


def getFunction():
	while True:
		string = ''
		try:
			string = raw_input("Type in the f(t,y) function: ")	 # get expression as string
			expr = sp.sympify(string)							   # turn string expression into Sympy expression
			break
		except:
			print "Please try again, invalid input: {}", string

	return expr

def getPoint(k):

	if k is None:							    # in case the user doesn't want to specify which point they're getting
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

	h = input("Type in the step h: ")				       # gets h as number
	n = input("Type in the number of iterations n: ")       # gets h as number

	return h, n

def plot(method):
	p = subprocess.Popen("cat {0}.conf | gnuplot".format(method), shell=True)
	os.waitpid(p.pid, 0)
	
	p = subprocess.Popen("xdg-open {0}.png".format(method), shell=True)
	os.waitpid(p.pid, 0)
	

	
def generateGnuPlotConf(pts, method):
	# write points to file:
	
	f = open('euler_points.txt', 'w')
	f.writelines(pts)
	f.close()
	
	# generate gnuplot configuration file:
	conf = ['set terminal png truecolor \n',
			'set output "METHOD.png" \n',
			'set autoscale \n',
			'set style data lines\n',
			'plot "METHOD_points.txt" using 1:2 title "METHOD"']
	
	conf = [x.replace('METHOD', method) for x in conf]
	f = open('euler.conf', 'w')
	f.writelines(conf)
	f.close()


def main():
	f = getFunction()
	
	t, y = getPoint(0)
	
	h, n = getNandH()
	
	points = euler(f, t, y, h, n)
	
	generateGnuPlotConf(points, 'euler')
	
	plot('euler')
	
	print "Have a great day"
	
	return

main()