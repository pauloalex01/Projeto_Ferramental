import time
from barcode.decoder_cam import Leitor_codigo
from database.banco_de_dados import Database
from services.service import *


if __name__ == "__main__":

    Database.criar_banco()

    leitor = Leitor_codigo()

    ferr_service = FerramentaService()
    mat_service = MatriculaService()
    mov_service = MovimentacaoService()

    fer_repo = FerramentaRepository()
    mat_repo = MatriculaRepository()
    movi_repo = MovimentacaoRepository()

    print("Iniciando...")
    time.sleep(1)
    print("Iniciando testes...\n")

    while True:

        try:
            opcao = int(input(
            """
            ===== MENU PRINCIPAL =====

            1 - Matrícula
            2 - Ferramenta
            3 - Movimentação
            4 - Ler código (câmera)
            5 - Encerrar

            Digite sua opção: 
            """))

        except ValueError:
            print("Digite um número válido.")
            continue


        # ================= MATRÍCULA =================

        if opcao == 1:

            sub = int(input(
            """
            ---- MATRÍCULA ----

            1 - Cadastrar
            2 - Remover
            3 - Buscar
            4 - Desativar
            5 - Voltar

            Escolha: 
            """))

            if sub == 1:
                matricula = input("Digite a matrícula: ")
                nome = input("Digite o nome: ")
                busca = mat_service.cadastrar(matricula, nome)
                print("Matrícula cadastrada.\n")


            elif sub == 2:
                matricula = input("Digite a matrícula: ")
                mat_service.remover(matricula)
                print("Matrícula removida.\n")

            elif sub == 3:
                matricula = input("Digite a matrícula: ")
                resultado = mat_repo.buscar_por_matricula(matricula)
                print(resultado)

            elif sub == 4:
                matricula = input("Digite a matrícula: ")
                mat_repo.desativar(matricula)
                print("Matrícula desativada.\n")


        # ================= FERRAMENTA =================

        elif opcao == 2:

            sub = int(input(
            """
            ---- FERRAMENTA ----

            1 - Cadastrar
            2 - Remover
            3 - Buscar
            4 - Desativar
            5 - Voltar

            Escolha: 
            """))

            if sub == 1:
                ferramenta = input("Digite o código da ferramenta: ")
                descricao = input("Digite a descrição: ")
                ferr_service.cadastrar(ferramenta, descricao)
                print("Ferramenta cadastrada.\n")

            elif sub == 2:
                ferramenta = input("Digite o código da ferramenta: ")
                ferr_service.remover(ferramenta)
                print("Ferramenta removida.\n")

            elif sub == 3:
                ferramenta = input("Digite o código da ferramenta: ")
                resultado = fer_repo.buscar_por_codigo(ferramenta)
                print(resultado)

            elif sub == 4:
                ferramenta = input("Digite o código da ferramenta: ")
                fer_repo.desativar(ferramenta)
                print("Ferramenta desativada.\n")


        # ================= MOVIMENTAÇÃO =================

        elif opcao == 3:

            sub = int(input(
            """
            ---- MOVIMENTAÇÃO ----

            1 - Emprestar
            2 - Devolver
            3 - Histórico
            4 - Voltar

            Escolha:
            """))

            if sub == 1:
                matricula = input("Matrícula: ")
                ferramenta = input("Código da ferramenta: ")
                mov_service.emprestar(matricula, ferramenta)
                print("Empréstimo realizado.\n")

            elif sub == 2:
                matricula = input("Matrícula: ")
                ferramenta = input("Código da ferramenta: ")
                mov_service.devolver(ferramenta)
                print("Ferramenta devolvida.\n")

            elif sub == 3:
                historico = "trabalhando nisso"
                print(historico)


        # ================= LEITOR DE CÓDIGO =================

        elif opcao == 4:

            print("Abrindo leitor...")
            codigos = leitor.executar()

            print("Códigos detectados:")
            for codigo in codigos:
                print(codigo)


        # ================= ENCERRAR =================

        elif opcao == 5:

            print("Encerrando sistema...")
            time.sleep(1)
            break

        else:
            print("Opção inválida.\n")