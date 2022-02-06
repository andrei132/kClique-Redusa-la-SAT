# Verifica daca exista o clica de marimea k in graf cu ajutorul 
# unei functii recursive(backtracking algorithm).
def kClique(grafNodes,k,curentK,clique,returnValue):

    # Daca curentK e mai mare decat k, nu mai are sens sa continui
    if(curentK > k):
        return False
    
    # Daca clica e de marimea potrivita verifica daca e clica
    if(curentK == k):
        return checkClikue(clique)

    # Incerc cu toate nodurile sa fac o clica
    for nod in grafNodes:
        try:
            [ x.name for x in clique ].index(nod.name)
            continue

        except:
            # Formez clica pentru urmatoarea apelare
            clique.append(nod)
            curentK += 1
            if kClique(nod.linkedNodes,k,curentK,clique,returnValue):
                return True
            clique.pop()
            curentK -= 1

    return returnValue

# Verifica daca nodurile primite ca parametru formeaza o clica
def checkClikue(possibleClique):

    # Parcurg toate noduriule si verific daca au legatura
    for node in possibleClique:
        for node2 in possibleClique:  
            if(node2.name == node.name):
                continue
            
            exist = False
            for x in node.linkedNodes:
                if(x.name == node2.name):
                    exist = True
                    break
            
            if not exist:
                return False

    return True
