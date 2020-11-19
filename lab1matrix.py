import random

class Generator:
    
    def generateGraph(self, n):
        newGraph = Graph(n)
        i = 0
        while(i < n-1):
            newGraph.addEdge(random.randint(0,i),i + 1, random.randint(1,50))
            i = i + 1
        return newGraph

class Graph:
    def __init__(self, n):
        self.matrix = []
        self.n = n
        
        i = 0
        while (i < n):
            j = 0
            tempMatrix = []
            while(j < n):
                tempMatrix.append(0)
                j = j + 1
            self.matrix.append(tempMatrix)
            i = i + 1

    def addEdge(self,frm,to,weight):
        if(weight < 0) or frm == to or frm >= len(self.matrix) or to >= len(self.matrix):
            raise Exception
        self.matrix[frm][to]=weight
        self.matrix[to][frm]=weight

    def checkEdge(self,node):
        if (len(self.matrix) < node):
            raise Exception
        i = 0
        for weight in self.matrix[node]:
            if(weight != 0):
                print(node, " is connected with ", i, " with weight ", weight)
            i = i + 1

    def print(self):
        print(self.matrix)

    def checkConnectivity(self, node):
        visited = [False] * self.n
        queue = []
        queue.append(node)
        visited[node] = True
        
        while(len(queue) > 0):
            value = queue.pop(0)

            i = 0
            while i < len(self.matrix[value]):
                if visited[i] == False and self.matrix[value][i] > 0:
                    queue.append(i)
                    visited[i] = True
                i = i + 1

        for x in visited:
            if(x == False):
                return False
        return True


# Generating a connected, undirected, weighted graph. Randomized edges and connections. 
ng = Generator()
grapho = ng.generateGraph(20000)
# print(grapho.checkConnectivity(3))
