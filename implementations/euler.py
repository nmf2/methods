
def euler(f, t, y, h, n):
	points = ["{0} {1}\n".format(t, y)]  # save point as a string with the following format: "t y\n"
	
	for i in range(n):
		k1 = f.subs('y', y).subs('t', t)  # substitute y then t
		y = y + h * k1
		t = t + h
		
		points.append("{0} {1}\n".format(t, y))
	
	return points
