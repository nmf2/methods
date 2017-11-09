from sympy import Point2D
from sympy import solvers
from sympy import Eq
from sympy.abc import y as s_y


def method(f, p, h, n, order):
    print "Running Adams-Moulton of order {} for {} iterations".format(order, n)
        
    points = []
    ys = []
    ts = []
    y = 0

    # setup first point
    for i in range(order - 2):
        points.insert(0,"{0} {1}\n".format(float(p[i].x), float(p[i].y)))
        ys.insert(0, p[i].y)
        ts.insert(0, p[i].x)
    
    p.insert(0,Point2D(p[0].x + h, s_y))                                   # add point (tn+1, yn+1), where yn+1 is a symbol

    if order == 1:
        for i in range(n):
            fk = calc_fk(f, p)
            expr = Eq(s_y, p[1].y + h * fk[0])

            y = solvers.solve(expr)                                                             # solve equation
            
            p[0] = Point2D(p[0].x, y[0])                                                        # save result of the equation as a point
            
            p.insert(0, Point2D(p[0].x + h, s_y))                                               # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                                           # removes the last item of the list fn
            
            points.append( "{0} {1}\n".format(float(p[1].x), float(p[1].y)))
            ys.append(p[1].y)
            ts.append(p[1].x)
        return points, ys, ts
        
    if order == 2:
        for i in range(n):
            fk = calc_fk(f, p)
            expr = Eq(s_y, p[1].y + (h/2)*( fk[0] + fk[1] ))
            
            y = solvers.solve(expr)                                                             # solve equation
            
            p[0] = Point2D(p[0].x, y[0])                                                        # save result of the equation as a point
            
            p.insert(0, Point2D(p[0].x + h, s_y))                                               # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                                           # removes the last item of the list fn
            
            points.append( "{0} {1}\n".format(float(p[1].x), float(p[1].y)))
            ys.append(p[1].y)
            ts.append(p[1].x)
        return points, ys, ts
    if order == 3:
        for i in range(n):
            fk = calc_fk(f, p)
            expr = Eq(s_y, p[1].y + (h/12)*( (5)*fk[0] + (8)*fk[1] - (1)*fk[2] ))
            
            y = solvers.solve(expr)                                                             # solve equation
            
            p[0] = Point2D(p[0].x, y[0])                                                        # save result of the equation as a point
            
            p.insert(0, Point2D(p[0].x + h, s_y))                                               # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                                           # removes the last item of the list fn
            
            points.append( "{0} {1}\n".format(float(p[1].x), float(p[1].y)))
            ys.append(p[1].y)
            ts.append(p[1].x)
        return points, ys, ts
        
    if order == 4:
        for i in range(n):
            fk = calc_fk(f, p)
            
            expr = Eq(s_y, p[1].y + (h/24)*( (9)*fk[0] + (19)*fk[1] - (5)*fk[2] + (1)*fk[3]))   # equation with implicit y to be solved

            y = solvers.solve(expr)                                                             # solve equation
            
            p[0] = Point2D(p[0].x, y[0])                                                        # save result of the equation as a point
            
            p.insert(0, Point2D(p[0].x + h, s_y))                                               # inserts the point that was just found into the beginning of the list
            p.pop(-1)
                                                                                    # removes the last item of the list fn
            points.append( "{0} {1}\n".format(float(p[1].x), float(p[1].y)))
            ys.append(p[1].y)
            ts.append(p[1].x)
        return points, ys, ts

    if order == 5:
        for i in range(n):
            fk = calc_fk(f, p)
            expr = Eq(s_y, p[1].y + (h/720)*( (251)*fk[0] + (646)*fk[1] - (264)*fk[2] + (106)*fk[3] - (19)*fk[4]))
            
            y = solvers.solve(expr)                                                             # solve equation
            
            p[0] = Point2D(p[0].x, y[0])                                                        # save result of the equation as a point
            
            p.insert(0, Point2D(p[0].x + h, s_y))                                               # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                                           # removes the last item of the list fn
            
            points.append( "{0} {1}\n".format(float(p[1].x), float(p[1].y)))
            ys.append(p[1].y)
            ts.append(p[1].x)
        return points, ys, ts
        
    if order == 6:
        for i in range(n):
            fk = calc_fk(f, p)

            expr = Eq(s_y, p[1].y + (h/1440)*( (475)*fk[0] + (1427)*fk[1] - (798)*fk[2] + (482)*fk[3] - (173)*fk[4] + (27)*fk[5]))

            y = solvers.solve(expr)                                                             # solve equation
            
            p[0] = Point2D(p[0].x, y[0])                                                        # save result of the equation as a point
            
            p.insert(0, Point2D(p[0].x + h, s_y))                                               # inserts the point that was just found into the beginning of the list
            p.pop(-1)                                                                           # removes the last item of the list fn
            
            points.append( "{0} {1}\n".format(float(p[1].x), float(p[1].y)))
            ys.append(p[1].y)
            ts.append(p[1].x)
        return points, ys, ts

def calc_fk(f, p):
    # Calculates each one of the fn+j, fn+j-1... values of the function
    #print 'entered calc_fk'
    fk = []
    for point in p:
        fk.append(f.subs('t', point.x).subs('y', point.y))   # calculate each fk
        
    # fk[0] = fn, fk[1] = fn-1... fk[j] = fn-j
    # print 'fk: ',fk
        
    return fk