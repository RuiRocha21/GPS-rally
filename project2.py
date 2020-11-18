import rallyDakar_v1
import gerador_grafo_tarefa1
import gerador_grafo_tarefa2


if __name__ == "__main__":

    opcao=0
    while('4' != opcao):
        print("Menu:")
        print("1 -> Gerar grafo tarefa 1 (0->1 == 1->0)")
        print("2 -> Gerar grafo tarefa 2 (0->1 != 1->0)")
        print("3 -> Gerar caminho de um grafo")
        print("4 -> Sair")
        opcao= input("Insira a opção: ")

        if opcao == '1':
            tarefa=1
            n_cidades = int(input("numero de cidades "))
            caso_teste = gerador_grafo_tarefa1.grafo(tarefa, n_cidades)
            op=0
            while ('2' != op):
                print("Menu:")
                print("1 -> Gerar caminho do grafo")
                print("2 -> Voltar ao menu anterior")
                op = input("")
                if op == '1':
                    rallyDakar_v1.rally(caso_teste, tarefa, n_cidades)
                    op = 2
                elif op == '2':
                    print("...")
                else:
                    print("opcao errada !!")

        elif opcao == '2':
            tarefa = 2
            n_cidades = int(input("numero de cidades "))
            caso_teste = gerador_grafo_tarefa2.grafo(tarefa, n_cidades)

            op = 0
            while ('2' != op):
                print("Menu:")
                print("1 -> Gerar caminho do grafo")
                print("2 -> Voltar ao menu anterior")
                op = input("")
                if op == '1':
                    rallyDakar_v1.rally(caso_teste, tarefa, n_cidades)
                    op = 2
                elif op == '2':
                    print("...")
                else:
                    print("opcao errada !!")

        elif opcao == '3':
            tarefa = input('número da tarefa ')
            cidades = input('número de cidades ')
            if cidades > '1':
                nome_ficheiro = "tarefa_"+str(tarefa)+"_"+str(cidades)+".txt"
                rallyDakar_v1.rally(nome_ficheiro, tarefa, cidades)

            else:
                print('número de cidades tem ser maior do que 1')

        elif opcao == '4':
            print("A sair....")
        else:
            print("opcao errada!!")