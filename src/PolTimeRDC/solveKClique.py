# Transformata descrisa in Readme, complexitate polinomiala
def kClique(graf,k):
    
    # Extrag din graf toata informatia necesara
    grafNode = graf.nodes
    nrNode = graf.nrNodes
    returnString = ""

    # Scriu clauzele care ar decide nodul j pe pozitia i in clica
    for i in range(k):
        returnString += "("
        for j in range(nrNode):
            returnString += "x" + str(j) + "x" + str(i) + " V "
        
        returnString = returnString[:-3]
        returnString+=") ^ "

    # Clauzele care verifica ca acelasi nod sa nu se afle in clica pe pozitii diferite
    # ca si cum acelasi nod e de mai multe ori prezent
    for i in range(nrNode):
        for j in range(k):
            for g in range(j):
                returnString += "(~x" + str(i) + "x" + str(g) + " V ~x" + str(i) + "x" + str(j) + ") ^ "

    # Clauzele care verifica daca nodurile nu au legatura sa nu fie ambele in clica
    for node in grafNode:
        notLinkedNode = [x for x in grafNode if (x not in node.linkedNodes) and x.name != node.name]
        for node2 in notLinkedNode:
            for g in range(k):
                for r in range(g):
                    returnString+="(~x" + str(node.name) + "x" + str(r)+" V ~x" + str(node2.name) + "x" + str(g)+") ^ "
        
    returnString = returnString[:-3]

    return returnString