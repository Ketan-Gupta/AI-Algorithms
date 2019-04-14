import math
import numpy as np

def estimate_coeff(x,y):
    n = np.size(x)
    mean_x, mean_y = np.mean(x), np.mean(y)

    SSxy = np.sum(y*x)- n*mean_x*mean_y
    SSxx = np.sum(x*x) - n*mean_x*mean_x
    
    b1 = SSxy/SSxx
    b2 = mean_y - b1*mean_x
    return (b1,b2)

def driver():
    x = np.array([10,9,2,15,10,16,11,16])
    y = np.array([95,80,10,50,45,98,38,93])
    
    b1,b2=estimate_coeff(x,y)
    print("b1 : {} b2 : {}".format(b1,b2))
    test_y = float(input("Enter the value of Y\n"))
    print("Predicted X :", b1*test_y+b2)


driver()

