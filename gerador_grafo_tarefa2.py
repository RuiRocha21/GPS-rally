from random import shuffle
from random import randint


def grafo(tarefa, n_cidades):
    fich = "tarefa_" + str(tarefa) + "_" + str(n_cidades) + ".txt"

    lista = list(range(1, (n_cidades)*(n_cidades)+1))

    shuffle(lista)
    print(lista)

    start = randint(0, n_cidades-1)

    f=open(fich,'w')
    f.write("start in " + str(start)+'\n')
    i=0

    for elem in range(n_cidades):

        j=0
        while j < (n_cidades):
            if j != elem:
                a=lista.pop(i)
                f.write(str(elem)+" -> "+str(j)+" "+str(a)+ '\n')
            j+=1

    f.close()

    return fich