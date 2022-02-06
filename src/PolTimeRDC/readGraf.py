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

# Citesc toate liniile
lines = file.readlines()

# Toate nodurile
nodes = []
k = int(lines[0])
nrNodes = int(lines[1])

# Aloc nodurile
for node in range(nrNodes):
    nodes.append(Nod(node))

# Aloc uin graf cu id 0, numar de noduri nrNodes si nosudurile nodes
graf = Graf(0,nrNodes,nodes)

# Salvez toate legaturile, cu conditia ca nodurile incep de la 0
for line in lines[3:]:
    linkNodes = line.split(" ")
    first = int(linkNodes[0]) - 1
    second = int(linkNodes[1]) - 1

    index1 = [ x.name for x in nodes ].index(first)
    index2 = [ x.name for x in nodes ].index(second)
    
    nodes[index1].addNode(nodes[index2])
    nodes[index2].addNode(nodes[index1])

res = solveKClique.kClique(graf,k)
print(res)