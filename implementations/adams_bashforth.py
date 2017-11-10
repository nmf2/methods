from sympy import Point2D

def method(f, p, h, n, order):
    print "Running Adams-Bashforth of order {} for {} iterations".format(order, n)
        
    points = []
    y = 0
    ys = []
    ts = []
    for i in range(order):
        points.insert(0, "{0} {1}\n".format(float(p[i].x), float(p[i].y)))
        ys.insert(0, p[i].y)
        ts.insert(0, p[i].x)
        
    if order == 1:
        for i in range(n + order -1):
            fk = calc_fk(f, p)
            
            y = p[0].y + h * fk[0]

            p.insert(0, Point2D(float(p[0].x + h), float(y)))           # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                   # removes the last item of the list
            
            points.append("{0} {1}\n".format(float(p[0].x), float(p[0].y)))
            ts.append(p[0].x)
            ys.append(p[0].y)
            print "y(%.4f) = %.7f" %(ts[-1], ys[-1])
            
        return points, ys, ts
        
    if order == 2:
        for i in range(n + order -1):
            fk = calc_fk(f, p)
            
            y = p[0].y + (h/2)*( (3)*fk[0] - fk[1] )
            
            p.insert(0, Point2D(float(p[0].x + h), float(y)))           # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                   # removes the last item of the list
            
            points.append("{0} {1}\n".format(float(p[0].x), float(p[0].y)))
            ts.append(p[0].x)
            ys.append(p[0].y)
            print "y(%.4f) = %.7f" %(ts[-1], ys[-1])
            
        return points, ys, ts
        
    if order == 3:
        for i in range(n + order-1):
            fk = calc_fk(f, p)
            y = p[0].y + (h/12)*( (23)*fk[0] - (16)*fk[1] + (5)*fk[2] )
            
            p.insert(0, Point2D(float(p[0].x + h), float(y)))           # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                   # removes the last item of the list
            
            points.append("{0} {1}\n".format(float(p[0].x), float(p[0].y)))
            ts.append(p[0].x)
            ys.append(p[0].y)
            print "y(%.4f) = %.7f" %(ts[-1], ys[-1])
            
        return points, ys, ts
        
    if order == 4:
        for i in range(n):
            fk = calc_fk(f, p)

            y = p[0].y + (h/24)*( (55)*fk[0] - (59)*fk[1] + (37)*fk[2] - (9)*fk[3])
        
            p.insert(0, Point2D(float(p[0].x + h), float(y)))           # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                   # removes the last item of the list fn
        
            points.append("{0} {1}\n".format(float(p[0].x), float(p[0].y)))
            ts.append(p[0].x)
            ys.append(p[0].y)
            print "y(%.4f) = %.7f" %(ts[-1], ys[-1])
            
        return points, ys, ts

    if order == 5:
        for i in range(n):
            fk = calc_fk(f, p)
            
            y = p[0].y + (h/720)*( (1901)*fk[0] - (2774)*fk[1] + (2616)*fk[2] - (1274)*fk[3] + (251)*fk[4])
            
            p.insert(0, Point2D(float(p[0].x + h), float(y)))           # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                   # removes the last item of the list
            
            points.append("{0} {1}\n".format(float(p[0].x), float(p[0].y)))
            ts.append(p[0].x)
            ys.append(p[0].y)
            print "y(%.4f) = %.7f" %(ts[-1], ys[-1])
            
        return points, ys, ts
        
    if order == 6:
        for i in range(n):
            fk = calc_fk(f, p)
            
            y = p[0].y + (h/1440)*( (4277)*fk[0] - (7923)*fk[1] + (9982)*fk[2] - (7298)*fk[3] + (2877)*fk[4] - (475)*fk[5])

            p.insert(0, Point2D(float(p[0].x + h), float(y)))           # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                   # removes the last item of the list
            
        
            points.append("{0} {1}\n".format(float(p[0].x), float(p[0].y)))
            ts.append(p[0].x)
            ys.append(p[0].y)
            print "y(%.4f) = %.7f" %(ts[-1], ys[-1])
            
        return points, ys, ts


def calc_fk(f, p):
    # Calculates each one of the fn+j, fn+j-1... values of the function
    #print 'entered calc_fk'
    fk = []
    for point in p:
        fk.append(float(f.subs('t', point.x).subs('y', point.y)))   # calculate each fk
        
    # fk[0] = fn, fk[1] = fn-1... fk[j] = fn-j
    #print 'fk: ',fk
        
        
    return fk
