from modules import util
import math

class Graph:

    def __init__(self):
        self.points = []
        self.weights = []

    def addPoint (self, x, y):
        self.points.append([x, y])

    def printPoints(self):
        print("Points in set: ")
        for i in range(len(self.points)):
            print(self.points[i])

    def findDistance(self, point1, point2):
        #Pythagorean theorum between the two points
        dist = math.sqrt(((self.points[point1][0] - self.points[point2][0]) ** 2 )+ ((self.points[point1][1] - self.points[point2][1]) ** 2 ))
        #cast to int before returning
        return int(dist)

    def calculateWeights(self):
        for i in range(len(self.points)):
            #For each row, append another row
            self.weights.append([])

            #calculate the distance between every point
            for j in range(len(self.points)):
                self.weights[i].append(self.findDistance(i, j))

        print("Calculated Weights: ")
        print(self.weights)   


    def calculateMST(self):
        #Fill in weights before proceeding
        self.calculateWeights

        #
        🖖🏿



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
    currentGraph.calculateMST()




