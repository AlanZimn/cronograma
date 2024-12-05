# Lista para armazenar tarefas
cronograma = []

# Função para adicionar uma tarefa
def adicionar_tarefa(nome, prazo):
    tarefa = {"nome": nome, "prazo": prazo}
    cronograma.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para listar as tarefas
def listar_tarefas():
    if not cronograma:
        print("Nenhuma tarefa no cronograma.")
    else:
        print("\n--- Cronograma ---")
        for i, tarefa in enumerate(cronograma):
            print(f"{i+1}. {tarefa['nome']} - Prazo: {tarefa['prazo']}")
        print("------------------")

# Função para excluir uma tarefa
def excluir_tarefa(indice):
    if 0 <= indice < len(cronograma):
        tarefa_removida = cronograma.pop(indice)
        print(f"Tarefa '{tarefa_removida['nome']}' removida com sucesso!")
    else:
        print("Índice inválido. Nenhuma tarefa foi removida.")

