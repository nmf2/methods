def method(f, t, y, h, n):
    print "Running Runge-Kutta"
    ts = [t]
    ys = [y]
    #points = ["{0} {1}\n".format(t, y)]  # save point as a string with the following format: "t y\n"
    
    for i in range(n):
        k1 = f.subs('t',t).subs('y',y)
        k2 = f.subs('t', t + h/2).subs('y',  k1 * h/2 + y)
        k3 = f.subs('t', t + h / 2).subs('y', k2 * h / 2 + y)
        k4 = f.subs('t', t + h ).subs('y', k3 * h + y)
        
        y = y + h*(k1 + 2*k2 + 2*k3 + k4)/6
        t = t + h
    
        ts.append(t)
        ys.append(y)
        print "y(%.4f) = %.7f" % (ts[-1], ys[-1])
    return ts, ys