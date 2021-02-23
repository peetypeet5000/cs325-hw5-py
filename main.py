from modules import util

class Graph:
    x = []
    y = []
    def __init__(self):
        self.x = []
        self.y = []

    def addPoint (self, x, y):
        self.x.append(x)
        self.y.append(y)

    def printPoints(self):
        print("Points in set: ")
        for i in range(len(self.x)):
            print("X: ", self.x[i], " Y: ", self.y[i])



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




