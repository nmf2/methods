# Methods
    Implementation of a few numerical methods for the Computational Numerical Methods 
    discipline from CIn-UFPE

# Installing dependencies
    1. Open the terminal and navigate to the root of the project (i.e. methods)
    2. Execute: 
        sudo make
    * This will make sure all the libraries are installed as well as the package 
      python-tk. 
      
    * If you don't have 'make' install with: sudo apt-get install make

# Running a method
    1. Run: python2 start.py
    * Suggestion:
        To save time you can make the input once and copy and paste it for each of the
        SINGLE step methods. For example:
            1 - t + 4*y
            0
            1
            .1
            10    
        If you copy and paste these four lines when selecting any single step method
        the function 1 - t + 4*y, with (t0,y0) = (0, 1), h = .1 and number of steps 10
        will be appoximated.
        
        For the multi step methods, all the initial points must be given. For example:
            1 - t + 4*y
            0
            1
            .1
            1.6089333
            .2
            2.5050062
            .3
            3.8294145
            .1
            10
        This is a valid input for Adams Bashforth of fourth order, if you notice there
        are 4 points: (0,1); (.1, 1.6..); (.2, 2.5..); (.3, 3.82..)
        That is necessary because it's fourth order.
        
        For Adams Moulton if the order is n > 1 then you only need n-1 points ( if the
        order is n = 1, then you need one point)
        
    2. After the method is selected the calculations will be made and a plot of the
       data will be shown. Also, the points will be displayed in the terminal while
       the plot is opened   
    
# Final (AND MOST IMPORTANT) Step
    1. Test all the methods and give me 100% in the project.
    2. Be happy :)