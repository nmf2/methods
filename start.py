
print 'Importing some stuff, wait for it, please...'
import utils
import os
from implementations import *


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
                    5) Adams-Bashforth Method                   * You'll choose the degree later
                    6) Adams-Moulton Method                     * You'll choose the degree later
                    7) All methods in the same graph
                    
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
            order = utils.getOrder()
            utils.runAdamsBash(order)
            
        elif method == 6:
            os.system('clear')
            print 'Selected Adams-Moulton Method\n'
            order = utils.getOrder()
            print 'Great! Making calculations, soon the plot will be shown. Hold on, please..'
            utils.runAdamsMoulton(order)
        elif method == 7:
            os.system('clear')
            print 'Selected All Single Step methods\n'
            print 'For the Adams-Moulton and Adams-Bashforth methods:\n'
            order = utils.getOrder()
            print 'Great! Making calculations, soon the plot will be shown. Hold on, please..'
            utils.runAllMethods(order)
        method = getMethod()

main()