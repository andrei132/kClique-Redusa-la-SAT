def kClique(graf,k):
    
    grafNode = graf.nodes
    nrNode = graf.nrNodes
    returnString = ""

    for i in range(k):
        returnString += "("
        for j in range(nrNode):
            returnString += "x" + str(j) + "x" + str(i) + " V "
        
        returnString = returnString[:-3]
        returnString+=") ^ "

    for i in range(nrNode):
        for j in range(k):
            for g in range(j):
                returnString += "(~x" + str(i) + "x" + str(g) + " V ~x" + str(i) + "x" + str(j) + ") ^ "

    for node in grafNode:
        notLinkedNode = [x for x in grafNode if (x not in node.linkedNodes) and x.name != node.name]
        for node2 in notLinkedNode:
            for g in range(k):
                for r in range(g):
                    returnString+="(~x" + str(node.name) + "x" + str(r)+" V ~x" + str(node2.name) + "x" + str(g)+") ^ "
        
    returnString = returnString[:-3]

    return returnString