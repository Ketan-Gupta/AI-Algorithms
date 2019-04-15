import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# b0 is slope c
# b1 is y intercept

def estimate_coeff(x,y):
    n = np.size(x)
    mean_x, mean_y = np.mean(x), np.mean(y)

    SSxy = np.sum(y*x)- n*mean_x*mean_y
    SSxx = np.sum(x*x) - n*mean_x*mean_x
    
    b1 = SSxy/SSxx
    b0 = mean_y - b1*mean_x
    return (b0,b1)

def plot_regression_line(x,y,b0,b1):
    plt.scatter(x,y,color="m",marker="o",s=30)
    y_pred = b0 + x*b1
    plt.plot(x,y_pred,color="g")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    exit()

def driver():
    data = pd.read_csv("Linear.csv")
    x = np.array(data.iloc[:,0])
    y = np.array(data.iloc[:,-1])
    #x = np.array([10,9,2,15,10,16,11,16])
    #y = np.array([95,80,10,50,45,98,38,93])
    b0,b1=estimate_coeff(x,y)
    print("b0 : {} b1 : {}".format(b0,b1))
    test_x = float(input("Enter the value of X\n"))
    print("Predicted Y :",b0 + b1*test_x) 
    plot_regression_line(x,y,b0,b1)



driver()

