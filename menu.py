from cronograma import adicionar_tarefa
from cronograma import listar_tarefas
from cronograma import excluir_tarefa

# Menu principal


while True:
    print("\n1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Excluir Tarefa")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Nome da Tarefa: ")
        prazo = input("Prazo: ")
        adicionar_tarefa(nome, prazo)
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        listar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
            excluir_tarefa(indice)
        except ValueError:
            print("Por favor, digite um número válido.")
    elif escolha == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")