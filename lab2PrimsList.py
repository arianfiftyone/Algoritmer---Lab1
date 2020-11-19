import random
import sys

class Generator:

    def generateGraph(self, n):
        newGraph = LinkedGraph(n)
        i = 0
        while i < n-1:
            newGraph.addWeight(random.randint(0,i),i + 1, random.randint(1,50))
            i = i + 1
        j = 0
        while j < n-1:
            frm = random.randint(0,j)
            to =j+1
            weight = random.randint(1,50)
            bish = newGraph.nodeArr[frm].searchEdge(-1)
            yeye = True
            for x in bish:
                if x.to == to:
                    yeye = False
            if(yeye == True):
                newGraph.addWeight(frm,to,weight)
            j = j + 1
        #self.printGeneratedGraph(newGraph.nodeArr)    
        return newGraph

    def printGeneratedGraph(self, graph):
        i = 0
        print("The random generated graph is:")
        for x in graph:
            currentNode = x.head
            while(currentNode != None):
                print(i, " is connected to ", currentNode.to, " with weight", currentNode.weight)
                currentNode = currentNode.next
            print()
            i = i + 1

class LinkedGraph:
    def __init__(self, n):
        self.n = n
        self.nodeArr = []
        i = 0
        while(i < n):
            self.nodeArr.append(LinkedList())
            i = i + 1
    
    def addWeight(self, frm, to, weight):
        if(weight < 0 or frm == to or frm >= self.n or to >= self.n):
            raise Exception
        currentLL = self.nodeArr[frm]
        currentLL.insertEdge(frm, to, weight)

        currentLL = self.nodeArr[to]
        currentLL.insertEdge(to, frm, weight)

    def getEdge(self, node):
        currentLL = self.nodeArr[node]
        currentLL.searchEdge(node)

    def MST(self, source):
        visited = [False] * self.n
        visited[source.to] = True
        possibleEdges = []
        mstSet = []
        mstSet.append(source)
        currentLL = self.nodeArr[source.to]
        tempList = currentLL.searchEdge(source.to)
        possibleEdges = possibleEdges + tempList

        while len(mstSet) < len(self.nodeArr):
            minWeight = sys.maxsize
            i = 0
            for x in possibleEdges:
                if x.getWeight() < minWeight:
                    minWeight = x.weight
                    indexMinWeight = i
                i += 1
            removedEdge = possibleEdges.pop(indexMinWeight)
            
            checkFrom = False
            checkTo = False
            
            for y in mstSet:
                if y.to == removedEdge.frm:
                    checkFrom = True
                if y.to == removedEdge.to:
                    checkTo = True

            if checkFrom == False or checkTo == False:
                mstSet.append(removedEdge)
                visited[removedEdge.to] = True
            edgesToBeAdded = self.nodeArr[removedEdge.to].searchEdge(-1)

            for z in edgesToBeAdded:
                if(visited[z.to] == False):
                    possibleEdges.append(z)

        return mstSet

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0
        self.curTrav = None
 
    def insertEdge(self, frm, to, weight):
        newNode = Node(frm, to , weight, self.head)
        self.head = newNode
        self.curTrav = newNode
        self.size = self.size + 1
        
    def traverse(self):
         self.curTrav = self.curTrav.next
        
    def searchEdge(self,node):
        edges = []
        if self.head == None:
            raise Exception
        currentSearch = self.head
        i = 0
        while(i < self.size):
            edges.append(currentSearch)
            currentSearch = currentSearch.next
            i = i + 1
        return edges
            
    def getHead(self):
        return self.head

    def resetTrav(self):
        self.curTrav = self.head

class Node:
    def __init__(self, frm, to, weight, next):
        self.frm = frm
        self.to = to
        self.weight = weight
        self.next = next

    def getNode(self):
        return self.to

    def getWeight(self):
        return self.weight

ng = Generator()
generate = ng.generateGraph(10000)

# grapho = LinkedGraph(8)
# grapho.addWeight(0,1,4)
# grapho.addWeight(1,2,3)
# grapho.addWeight(1,3,2)
# grapho.addWeight(3,4,1)
# grapho.addWeight(3,5,1)
# grapho.addWeight(4,5,1)
# grapho.addWeight(6,4,2)
# grapho.addWeight(7,5,2)
# grapho.addWeight(6,7,1)
# grapho.addWeight(2,7,4)
# grapho.addWeight(0,6,5)

mst = generate.MST(Node(None, 0, None, None))
# i = 1
# print("MST:")
# while i < len(mst):
#     print(mst[i].frm.__str__() + " is connected to " + mst[i].to.__str__() + " with weight " + mst[i].weight.__str__())
#     i +=1

