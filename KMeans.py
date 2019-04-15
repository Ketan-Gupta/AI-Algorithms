import math


def summation(container, value):
    total = 0
    for x in range(len(container)):
        total += container[x][value]
    return total

def euclidean_distance(first,second):
    # first and second =[1,2] typed list
    return math.sqrt((pow((first[0]-second[0]),2))+(pow((first[1]-second[1]),2)))

def knn(parentSet,median1,median2):
    prev_median1,prev_median2=median1,median2
    set1 = list()
    set2=list()

    for x in parentSet:
        if(euclidean_distance(median1,x)<euclidean_distance(median2,x)):
            set1.append(x)
        else:
            set2.append(x)

    new_median1 = summation(set1,0)/len(set1),summation(set1,1)/len(set1)
    new_median2 = summation(set2,0)/len(set2),summation(set2,1)/len(set2)



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
    
    print("Set1: Median=",new_median1)
    print(set1)
    print("Set2: Median=",new_median2)
    print(set2)

def driver():
    parentSet = [[0.1,0.6],[0.15,0.71],[0.08,0.9],[0.16,0.85],[0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]]
    median1, median2 = parentSet[0],parentSet[7]
    knn(parentSet, median1,median2)

driver()
