from modules import util
import math

class Graph:
    x = []
    y = []
    def __init__(self):
        self.x = []
        self.y = []
        self.weights = [[]]

    def addPoint (self, x, y):
        self.x.append(x)
        self.y.append(y)

    def printPoints(self):
        print("Points in set: ")
        for i in range(len(self.x)):
            print("X: ", self.x[i], " Y: ", self.y[i])

    def calculateWeights(self):
        self.weights = [[0 for i in range(len(self.x))] for j in range(len(self.y))] 
        for i in range(len(self.x)):
            for j in range(len(self.y)):
                self.weights[i][j] = int(math.sqrt(self.x[i] ** 2 + self.y[j] ** 2))

        print("Calculated Weights: ")
        print(self.weights)        



#For each test case, make a graph object


data = util.readFile()

#keep track of line, skip first line (num of cases)
lineInData = 0

for i in range(data[0][0]):
    print("Data Set: ", i + 1)
    currentGraph = Graph()
    lineInData += 1
    
    for j in range((data[lineInData][0])):
        lineInData += 1
        currentGraph.addPoint(data[lineInData][0], data[lineInData][1])
    
    currentGraph.printPoints()
    currentGraph.calculateWeights()




