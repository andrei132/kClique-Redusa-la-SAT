import sys
import solveKClique

class Nod:
    
    def __init__(self, name):
        self.name = name
        self.linkedNodes = []

    def addNode(self, node):
        self.linkedNodes.append(node)

class Graf:
    def __init__(self, id, nrNodes, nodes):
        self.id = id
        self.nrNodes = nrNodes
        self.nodes = nodes

try:
    fileName = sys.argv[1]

except:
    print("\nError: File name not specified\n")
    quit()

try:
    file = open(fileName, "r")

except FileNotFoundError as e:
    print(e)
    quit()

lines = file.readlines()

nodes = []
k = int(lines[0])
nrNodes = int(lines[1])

for node in range(nrNodes):
    nodes.append(Nod(node))

graf = Graf(0,nrNodes,nodes)

for line in lines[3:]:
    linkNodes = line.split(" ")
    first = int(linkNodes[0]) - 1
    second = int(linkNodes[1]) - 1

    index1 = [ x.name for x in nodes ].index(first)
    index2 = [ x.name for x in nodes ].index(second)
    
    nodes[index1].addNode(nodes[index2])
    nodes[index2].addNode(nodes[index1])

res = False
res = solveKClique.kClique(graf,k)
print(res)