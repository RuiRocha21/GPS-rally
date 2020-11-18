
import os
from sys import maxsize

from collections import defaultdict  # dictionary of lists
import time;

outputdebug = False
caminho=[]

def debug(msg):
    if outputdebug:
        print(msg)

# classe que representa um nó
class Node:

    def __init__(self, key):
        self.key = key

    def getKey(self):
        return self.key


# class that represents a graph
class Graph:

    def __init__(self):
        self.nodes = {} # dictionary of the nodes
        self.edges = []  # lista de 3-tuple (source, destination, weight)

        # dictionary with the lists of successors of each node, faster for get the successors
        # each item of list is a 2-tuple: (destination, weight)
        self.successors = defaultdict(list)


    # function that adds edges
    def addEdge(self, source, destination, weight):
        edge = (source, destination, weight) # creates tuple (3-tuple)
        if not self.existsEdge(edge): # adds edge if not exists
            self.nodes[source], self.nodes[destination] = source, destination # adds the nodes
            self.edges.append(edge) # adds edge
            self.successors[source.getKey()].append((destination, weight)) # adds successor
        else:
            print('Error: edge (%s -> %s with weight %s) already exists!!' \
                % (edge[0].getKey(), edge[1].getKey(), edge[2]))


    # function that checks if edge exists
    def existsEdge(self, edge):
        for e in self.edges:
            # compares source's key, destionation's key
            if e[0].getKey() == edge[0].getKey() and e[1].getKey() == edge[1].getKey():
                return True

        return False


    def procuraCaminho(self, node, visited, new_g_cost, num_cidades, nivel, goal_node):

        if node.getKey() == goal_node.getKey():
            #print('last  '+node.getKey()+' visited '+str(visited)+'  custo '+str(new_g_cost)+ ' len '+str(len(visited)))
            if caminho:
                #print(caminho)
                if caminho[0][1] > new_g_cost:
                    caminho.clear()
                    caminho.append((visited[:], new_g_cost))
            else:
                caminho.append((visited[:],new_g_cost))

        else:
            successors = self.successors[node.getKey()]
            nivel += 1
            for successor in successors:
                destination, weight = successor  #unpack 2-tuple successor
                #print(destination.getKey(),weight)
                if destination.getKey() not in visited and destination.getKey() != goal_node.getKey() and nivel!=(num_cidades+1):
                    new_g_cost = new_g_cost + weight
                    visited.append(destination.getKey())
                    if caminho:
                        if caminho[0][1] > new_g_cost:
                            self.procuraCaminho(destination, visited, new_g_cost, num_cidades, nivel, goal_node)

                    visited.remove(destination.getKey())
                    new_g_cost = new_g_cost - weight

                elif destination.getKey() not in visited and destination.getKey() == goal_node.getKey() and nivel == (num_cidades + 1):
                    new_g_cost = new_g_cost + weight
                    visited.append(destination.getKey())
                    if caminho:
                        if caminho[0][1] > new_g_cost:
                            self.procuraCaminho(destination, visited, new_g_cost, num_cidades, nivel, goal_node)

                    visited.remove(destination.getKey())
                    new_g_cost = new_g_cost - weight



    def inicia(self, initial_node, goal_node, num_cidades, tarefa):
        if not self.edges:
            print('Error: graph not contains edges!!')
        else:

            visited=[]
            nivel=1

            aux=0
            successors = self.successors[initial_node.getKey()]
            nivel += 1
            #print(int(len(successors))-1)
            for successor in successors:

                if aux<(int(len(successors))-1) and tarefa==1:
                    #print(aux)

                    aux+=1
                    destination, weight = successor  # unpack 2-tuple successor
                    new_g_cost = weight

                    visited.append(destination.getKey())
                    self.procuraCaminho(destination, visited, new_g_cost, num_cidades, nivel, goal_node)

                    visited.remove(destination.getKey())
                else:
                    destination, weight = successor  # unpack 2-tuple successor
                    #print(destination.getKey())
                    new_g_cost = weight

                    visited.append(destination.getKey())
                    self.procuraCaminho(destination, visited, new_g_cost, num_cidades, nivel, goal_node)
                    visited.remove(destination.getKey())

def rally(caso_teste, t, n_cidades):
    graph = Graph()

    # ref_arquivo = open("mapa.txt", "r")
    if not os.path.isfile(caso_teste):
        print("Ficheiro não encontrado!")
        return

    ref2_arquivo = open(caso_teste, "r")
    linhas = ref2_arquivo.readlines()
    ref2_arquivo.close()

    count = 0
    tarefa=int(t)

    num_cidades = int(n_cidades)

    node = [0] * (num_cidades + 1)

    for i in range(num_cidades + 1):
        node[i] = Node(str(i))

    num_linhas = len(linhas)
    # print("Numero de arestas  ", num_arestas, "numero de linhas ", num_linhas-1)


    matriz_init = [0] * (num_cidades + 1)

    start = 0
    for i in range(num_cidades + 1):
        matriz_init[i] = [0] * (num_cidades + 1)

    for linha in linhas:
        valores = linha.split()
        if count == 0:
            # print('starts ' + valores[2])
            start = int(valores[2])
        else:
            matriz_init[int(valores[0])][int(valores[2])] = int(valores[3])
            # print("1matriz init " + str(matriz_init[int(valores[0])][int(valores[2])]))
            if tarefa == 1:
                # print("2matriz init " + str(matriz_init[int(valores[2])][int(valores[0])]))
                matriz_init[int(valores[2])][int(valores[0])] = int(valores[3])
        count += 1


    for i in range(int(num_cidades)):
        for j in range(int(num_cidades)):
            if i != j:
                graph.addEdge(node[i], node[j], matriz_init[i][int(j)])


        #matriz_init[i][int(num_cidades)] = matriz_init[start][i]
        #if i != int(start):
        #    graph.addEdge(node[i], node[int(num_cidades)], matriz_init[i][int(num_cidades)])
            # print(matriz_init[i][:])

    print("Start: ", start)
    print("Número de cidades: ", num_cidades)
    #for i in range(num_cidades + 1):
    #    print(matriz_init[i][:num_cidades + 1])
    #t_init = time.clock()
    caminho.append(([], maxsize+1))
    graph.inicia(node[start],node[start], num_cidades, tarefa)
    #print(time.clock()-t_init)
    path = []
    inicio=[]
    inicio.append(str(start))
    minimo=maxsize+1
    for i in range (len(caminho)):
        if minimo > caminho[i][1]:
            minimo=caminho[i][1]

            path=inicio+caminho[i][0]

    if path:
        print(path[:], minimo)

    matriz_init.clear()
    caminho.clear()

