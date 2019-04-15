import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def summation(container, value):
    total = 0
    for x in range(len(container)):
        total += container[x][value]
    return total

def euclidean_distance(first,second):
    # first and second =[1,2] typed list
    return math.sqrt((pow((first[0]-second[0]),2))+(pow((first[1]-second[1]),2)))

def knn(parentSet,median1,median2,median3):
    prev_median1,prev_median2,prev_median3=median1,median2,median3
    set1 = list()
    set2 = list()
    set3 = list()

    for x in parentSet:
        if(euclidean_distance(median1,x)<euclidean_distance(median2,x) and euclidean_distance(median1,x)<euclidean_distance(median3,x)):
            set1.append(x)
        elif(euclidean_distance(median2,x)<euclidean_distance(median3,x)):
            set2.append(x)
        else:
            set3.append(x)

    new_median1 = summation(set1,0)/len(set1),summation(set1,1)/len(set1)
    new_median2 = summation(set2,0)/len(set2),summation(set2,1)/len(set2)
    new_median3 = summation(set3,0)/len(set3),summation(set3,1)/len(set3)


    while(prev_median1 != new_median1 and prev_median2 != new_median2):
        prev_median1,prev_median2 = new_median1,new_median2
        set1.clear()
        set2.clear()
        for x in parentSet:
            if(euclidean_distance(median1,x)<euclidean_distance(median2,x)):
                set1.append(x)
            else:
                set2.append(x)
        new_median1 = summation(set1,0)/len(set1),summation(set1,1)/len(set1)
        new_median2 = summation(set2,0)/len(set2),summation(set2,1)/len(set2)
        new_median3 = summation(set3,0)/len(set3),summation(set3,1)/len(set3)
    print("Set1: Median=",new_median1)
    print(set1)
    print("Set2: Median=",new_median2)
    print(set2)
    print("Set3: Median=",new_median3)
    print(set3)
    return (set1,set2,set3)

def driver():
    data = pd.read_csv("KMeans.csv")
    parentSet = list()
    for x in range(len(data)):
        parentSet.append([data.iloc[x][0],data.iloc[x][1]])
    #parentSet = [[0.1,0.6],[0.15,0.71],[0.08,0.9],[0.16,0.85],[0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]]
    median1, median2, median3 = parentSet[0],parentSet[7],parentSet[3]
    set1,set2,set3 = knn(parentSet, median1,median2,median3)
    plt_set1 = np.array(set1)
    plt_set2 = np.array(set2)
    plt_set3 = np.array(set3)
    plt.scatter(plt_set1[:,0],plt_set1[:,1])
    plt.scatter(plt_set2[:,0],plt_set2[:,1])
    plt.scatter(plt_set3[:,0],plt_set3[:,1])
    plt.show()
    exit()

driver()
