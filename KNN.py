import pandas as pd
import math
import operator


trainingSet = pd.read_csv("Training.csv")
def euclidean_distance(first,second,length):
    distance = 0
    for x in range(length):
        distance += pow((first[x]-second[x]),2) 
    return math.sqrt(distance)

def getNeighbours(trainingSet, testInstance, k):
    distances = list()
    neighbours = list()
    length = testInstance.shape[1]
    for x in range(len(trainingSet)):
        dist = euclidean_distance(testInstance, trainingSet.iloc[x],length)
        distances.append((trainingSet.iloc[x],dist))
    distances.sort(key=operator.itemgetter(1))
    for x in range(k):
        neighbours.append(distances[x][0].loc["Class"])
    return neighbours 

def getClassVotes(neighbours):
    classVotes = dict()
    sortedVotes = list()
    for x in range(len(neighbours)):
        if neighbours[x] in classVotes:
            classVotes[neighbours[x]]+=1
        else:
            classVotes[neighbours[x]]=1
   
    sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]

def driver():
    k=3
    test=[[6,6]]
    testInstance = pd.DataFrame(test)
    class_label = getClassVotes(getNeighbours(trainingSet, testInstance,k))
    print(class_label)


driver()



        



    



