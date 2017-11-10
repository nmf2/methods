from implementations import *
import utils
import os

def main():
    def getMethod():
        while True:
            try:
                os.system('clear')
                print """
                    Welcome!
                    
                    Please select which method you'd like to use:
                    1) Simple Euler Method
                    2) Inverse Euler Method
                    3) Improved Euler Method
                    4) Runge-Kutta Method
                    5) Adams-Bashforth Method                   * You'll chose the degree later
                    6) Adams-Moulton Method                     * You'll chose the degree later
                    
                    PS: To leave enter a different number
                """
                method = int(input("\nPlease input an integer: "))
                return method
            except:
                print "Please try again, invalid input."
        
    method = getMethod()
    while method in range(1,8):
        if method == 1:
            os.system('clear')
            print 'Selected Simple Euler Method\n'
            utils.runSimpleMethod(eulers.simple_euler, "Simple Euler Method")
            
        elif method == 2:
            os.system('clear')
            print 'Selected Inverse Euler Method\n'
            utils.runSimpleMethod(eulers.inverse_euler, "Inverse Euler Method")
            
        elif method == 3:
            os.system('clear')
            print 'Selected Improved Euler Method\n'
            utils.runSimpleMethod(eulers.improved_euler, "Improved Euler Method")
            
        elif method == 4:
            os.system('clear')
            print 'Selected Runge-Kutta Method\n'
            utils.runSimpleMethod(runge.method, "Runge-Kutta Method")
            
        elif method == 5:
            os.system('clear')
            print 'Selected Adams-Bashforth Method\n'
            while True:
                try:
                    order = int(input("\nPlease input the degree of the method: "))
                    break
                except:
                    print "Please try again, invalid input."
            utils.runAdamsBash(order)
            
        elif method == 6:
            os.system('clear')
            print 'Selected Adams-Moulton Method\n'
            while True:
                try:
                    order = int(input("\nPlease input the degree of the method: "))
                    break
                except:
                    print "Please try again, invalid input."
            utils.runAdamsMoulton(order)
        
        method = getMethod()

main()
