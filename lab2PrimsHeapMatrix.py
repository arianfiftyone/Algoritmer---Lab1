import random
import sys

class Generator:
    def generateGraph(self, n):
        newGraph = Graph(n)
        i = 0
        while i < n-1:
            newGraph.addEdge(random.randint(0,i),i + 1, random.randint(1,50))
            i = i + 1
        j = 0
        while j < n-1:
            frm = random.randint(0,j)
            to = j + 1
            weight = random.randint(1,50)
            bish = newGraph.checkEdge(frm)
            yeye = True
            for x in bish:
                if x.to == to:
                    yeye = False
            if(yeye == True):
                newGraph.addEdge(frm,to,weight)
            j = j + 1
        #self.printGeneratedGraph(newGraph.matrix)      
        return newGraph

    def printGeneratedGraph(self, graph):
        i = 0
        print("The random generated graph is:")
        for x in graph:
            j = 0
            for y in x:
                if(graph[i][j] > 0):
                    print(i, " is connected to ", j, " with weight: " , graph[i][j])
                j = j + 1
            print()
            i = i + 1

class Heap:
    def __init__(self, root):
        tempEdge = Edges(-1,-1, -1)
        self.heapList = []
        self.heapList.append(tempEdge)
        self.heapList.append(root)
    
    def minHeapify(self, node, i):
        if node.weight < self.heapList[i//2].weight:
            tempParent = self.heapList[i//2]
            self.heapList[i//2] = node
            self.heapList[i] = tempParent
            self.minHeapify(node, i//2)            

    def topHeapify(self, nodeWeight, i):
        left = 2*i
        right = 2*i+1
        
        if right >= len(self.heapList):
            return

        if nodeWeight <= self.heapList[left].weight and nodeWeight <= self.heapList[right].weight:
            return

        if  nodeWeight > self.heapList[left].weight:
            tempParent = self.heapList[i]
            self.heapList[i] = self.heapList[left]
            self.heapList[left] = tempParent

        if self.heapList[i].weight > self.heapList[right].weight:
            tempParent = self.heapList[i]
            self.heapList[i] = self.heapList[right]
            self.heapList[right] = tempParent

            self.topHeapify(nodeWeight, right)
        self.topHeapify(nodeWeight, left)

    def addNode(self, node):
        self.heapList.append(node)
        self.minHeapify(node, len(self.heapList)-1)
    
    def getMinEdge(self):
        if len(self.heapList) - 1 == 1:
            rValue = self.heapList.pop(-1)
        else:
            tempNode = self.heapList[1]
            self.heapList[1] = self.heapList[-1]
            self.heapList[-1] = tempNode 
            rValue = self.heapList.pop(-1)
            self.topHeapify(self.heapList[1].weight, 1)
        return rValue

class Edges:
    def __init__(self, frm, to, weight):
        self.frm = frm
        self.to = to
        self.weight = weight

    def getWeight(self):
        return self.weight
    def getTo(self):
        return self.to
     
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

    def checkEdge(self, node):
        edges = []
        i = 0
        for weight in self.matrix[node]:
            if(weight != 0):
                tempEdge = Edges(node, i, weight)
                edges.append(tempEdge)
            i = i + 1
        return edges

    def print(self):
        print(self.matrix)

    def MST(self, source):
        visited = [False] * self.n
        visited[source.to] = True
        mstSet = []
        mstSet.append(source)
        tempList = self.checkEdge(source.to)
        possibleEdges = Heap(tempList[0])

        i = 1
        while i < len(tempList):
            possibleEdges.addNode(tempList[i])
            i = i + 1

        while len(mstSet) < len(self.matrix):
            removedEdge = possibleEdges.getMinEdge()
            
            checkFrom = visited[removedEdge.to]
            checkTo = visited[removedEdge.frm]

            if checkFrom == False or checkTo == False:
                mstSet.append(removedEdge)
                visited[removedEdge.to] = True
            edgesToBeAdded = self.checkEdge(removedEdge.to)

            for z in edgesToBeAdded:
                if(visited[z.to] == False):
                    possibleEdges.addNode(z)
        return mstSet

ng = Generator()
generate = ng.generateGraph(10000)
    
# grapho = Graph(8)
# grapho.addEdge(0,1,4)
# grapho.addEdge(1,2,3)
# grapho.addEdge(1,3,2)
# grapho.addEdge(3,4,1)
# grapho.addEdge(3,5,1)
# grapho.addEdge(4,5,1)
# grapho.addEdge(6,4,2)
# grapho.addEdge(7,5,2)
# grapho.addEdge(6,7,1)
# grapho.addEdge(2,7,4)
# grapho.addEdge(0,6,5)

mst = generate.MST(Edges(None, 0, None))
# i = 1
# print("MST:")
# while i < len(mst):
#     print(mst[i].frm.__str__() + " is connected to " + mst[i].to.__str__() + " with weight " + mst[i].weight.__str__())
#     i +=1
