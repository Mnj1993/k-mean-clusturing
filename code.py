import sys
from sys import argv
import math
import copy
import sys
import random

################
##  py hw7.py datafile numberOfCluster
################

#####
## Calculate Mean
######
def calcMean():
    
    n = [0] * numK; ##Initialize array that holds number of rows for particular cluster
    #m = [[0] * dataCols for i in range(numK)]
    for i in range(0, numK, 1):
        for x in range(0, dataRows, 1):
            if(trainlabels.get(x) == i):
                n[i] = n[i] + 1;
                for j in range(0,dataCols,1):
                    #print("Cluster: ",i ,"Row: ",x," col : ",j);
                    #print("Value :", data[x][j]);
                    m[i][j] += data[x][j]

    for i in range(0,numK,1):
        for j in range(0,dataCols,1):
            if(n[i]!=0):
                m[i][j] /= n[i]
    #print("Mean: ",m)


#####
## Calculate distance
######
def calcDist(d, index, m):
    minValue = sys.maxsize
    minIndex = 0
    for i in  range (0, numK):
        distance = sum([(a - b) ** 2 for a, b in zip(d, m[i])])
        if(distance < minValue):
            minValue = distance
            minIndex = i
        #print("d: ", d, "Mean: ", m[i], " Cluster: ", i, "Distance: ",distance)
    trainlabels[index] = minIndex

################
##Read Data
################
f = open(argv[1])
data = []
l = f.readline()
while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()
dataRows = len(data)
dataCols = len(data[0])
f.close()

################
##Read Number of Clusters
###############
numK = int(sys.argv[2])

################
##Main
###############

##Initializing clusters
trainlabels={}
for x in range(0,dataRows):
    trainlabels[x]=random.sample(range(0, numK), 1)[0] 

#print("Initial Mean : ",m)
#print("Before Trainlabels : ",trainlabels)

lastObjective = 10000000
objective = lastObjective - 10
diff = 0.001
while(lastObjective - objective > diff):
    lastObjective = objective
    
    ##Initialize mean
    m0=[]
    for j in range(0,dataCols,1):
        m0.append(0)
    m=[]
    for i in range(0,numK,1):
        x = copy.deepcopy(m0)
        m.append(x)
        
    ##Calculate mean
    calcMean()
    #print("Mean: ",m)
    
    ##Calculate distance and classify cluster
    for i in range(0, dataRows):
        calcDist(data[i], i, m)
        #print("Iterate Trainlabels : ",trainlabels)
    #print("Trainlabels : ",trainlabels)

    ##Calculate objective
    total = 0
    for i in range(0, numK, 1):
        for j in range(0, dataRows, 1):
            if(trainlabels.get(j) == i):
                total += sum([(a - b) ** 2 for a, b in zip(data[j], m[i])])
    print("Total: ",total)
    objective = total


################
##Print statements
###############
for i in range(0, dataRows, 1):
    #if(trainlabels.get(i) != None):
    print(trainlabels[i], " ",i) 
#print("Data : ",data)
#print("Mean : ",m)
#print("After trainlabels : ",trainlabels)
