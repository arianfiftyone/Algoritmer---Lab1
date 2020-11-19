import random

class Generator:
    random.randint

    def generateGraph(self, n):
        newGraph = LinkedGraph(n)
        i = 0
        while(i < n-1):
            newGraph.addWeight(random.randint(0,i),i + 1, random.randint(1,50))
            i = i + 1
        return newGraph

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
        currentLL.insertEdge(to, weight)

        currentLL = self.nodeArr[to]
        currentLL.insertEdge(frm, weight)

    def getEdge(self, node):
        currentLL = self.nodeArr[node]
        currentLL.searchEdge(node)

    def checkConnectivity(self,node):
        visited = [False] * self.n
        queue = []
        queue.append(node)
        visited[node] = True
        
        while(len(queue) > 0):
            value = queue.pop(0)
            while(self.nodeArr[value].curTrav != None):
                i = self.nodeArr[value].curTrav.node
                if(visited[i] == False):
                    queue.append(i)
                    visited[i] = True
                self.nodeArr[value].traverse()
        for x in visited:
            if(x == False):
                return False
        for nodes in self.nodeArr:
            nodes.resetTrav()
        return True

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0
        self.curTrav = None
 
    def insertEdge(self, to, weight):
        newNode = Node(to , weight, self.head)
        self.head = newNode
        self.curTrav = newNode
        self.size = self.size + 1
        
    def traverse(self):
         self.curTrav = self.curTrav.next
        
    def searchEdge(self,node):
        if self.head == None:
            raise Exception
        currentSearch = self.head
        i = 0
        while(i < self.size):
            print(node , " is connected to ",currentSearch.getNode(), " with weight ", currentSearch.getWeight())
            currentSearch = currentSearch.next
            i = i + 1
            
    def getHead(self):
        return self.head

    def resetTrav(self):
        self.curTrav = self.head

class Node:
    def __init__(self, node, weight, next):
        self.node = node
        self.weight = weight
        self.next = next

    def getNode(self):
        return self.node

    def getWeight(self):
        return self.weight
 
# Generating a connected, undirected, weighted graph. Randomized edges and connections. 
ng = Generator()
grapho = ng.generateGraph(10)

# For printuot of all nodes and edges with weights
#  
# i = 0
# for x in grapho.nodeArr:
#     x.searchEdge(i)
#     i = i + 1
# print(grapho.checkConnectivity(2))
