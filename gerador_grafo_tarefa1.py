import random


def grafo(tarefa, n_cidades):
    fich = "tarefa_" + str(tarefa) + "_" + str(n_cidades) + ".txt"

    lista = list(range(1, int(((n_cidades) * (n_cidades - 1))/2)+1))
    random.shuffle(lista)

    print(lista)

    start = random.randint(0, n_cidades-1)
    f = open(fich, 'w')
    f.write("start in " + str(start) + '\n')
    i = 0

    for elem in range(n_cidades - 1):
        j = elem + 1

        while j < (n_cidades):
            a = lista.pop(i)
            f.write(str(elem) + " -> " + str(j) + " " + str(a) + '\n')
            j += 1

    f.close()

    return fich
