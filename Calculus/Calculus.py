#TRAPEZOID method
# the function to be integrated
def func(x):
    return x**3+x**2+x+1

# boundary of area
a = 1.
b = 10.
width = 0.1
# calculate the number of trapezoids
n = int((b - a) / width)

# define the variable for area
Area = 0

# loop to calculate the area of each trapezoid and sum.
for i in range(1, n+1):
    #the x locations of the left and right side of each trapezpoid
    x0 = a+(i-1)*width
    x1 = a+i*width

    #the area of each trapezoid
    Ai = width * (func(x0) + func(x1))/ 2.

    # sum the areas
    Area = Area + Ai

#print out the result.
print ("Area using trapezium method = ", Area)
# INTERGRATION METHOD
from scipy.integrate import quad

# boundary
ans, err = quad(func, 1, 10)
print ("Area using intergration =", ans)

#Percent error
pError = (Area - ans)/ ans *100
print ("Percent Error = ", pError,"%")

# Graphing the function
import numpy as np
import matplotlib.pyplot as plt

def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    plt.plot(x, y)
    plt.show()
graph(func, range(-10, 10))

