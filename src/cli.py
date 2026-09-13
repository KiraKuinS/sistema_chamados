from src.manager import GerenciadorChamados

def menu():
    sistema = GerenciadorChamados()

    while True:
        print("\n--- SISTEMA DE GESTÃO DE CHAMADOS ---")
        print("1. Criar Chamado")
        print("2. Listar Todos os Chamados")
        print("3. Atualizar Status")
        print("4. Buscar Chamados (por título, prioridade ou status)")
        print("5. Excluir Chamado")
        print("6. Sair")

        opcao = input("\nEscolha uma opção (1-6): ").strip()

        if opcao == "1":
            titulo = input("Título do chamado: ").strip()
            prioridade = input("Prioridade (Baixa, Média, Alta): ").strip().capitalize()
            
            if titulo:
                sistema.criar_chamado(titulo, prioridade)
            else:
                print("❌ O título do chamado não pode ser vazio.")

        elif opcao == "2":
            sistema.listar_chamados()

        elif opcao == "3":
            try:
                id_c = int(input("Informe o ID do chamado a atualizar: "))
                status = input("Novo status (Pendente, Em Andamento, Concluído): ").strip().capitalize()
                sistema.atualizar_status(id_c, status)
            except ValueError:
                print("❌ ID inválido. Digite apenas números inteiros.")

        elif opcao == "4":
            termo = input("Digite o termo de busca: ").strip()
            if termo:
                sistema.buscar_chamados(termo)
            else:
                print("❌ Digite ao menos uma palavra para buscar.")

        elif opcao == "5":
            try:
                id_c = int(input("Informe o ID do chamado a excluir: "))
                sistema.deletar_chamado(id_c)
            except ValueError:
                print("❌ ID inválido. Digite apenas números inteiros.")

        elif opcao == "6":
            print("\nEncerrando o sistema... Até logo!")
            break
            
        else:
            print("❌ Opção inválida. Tente novamente.")