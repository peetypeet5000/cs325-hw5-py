

def readFile(): 
    graphFile = open("graph.txt")

    #make to string
    fileString = graphFile.readlines()

    data = []
    for line in fileString:
        data.append([int(v) for v in line.split()])

    return data
