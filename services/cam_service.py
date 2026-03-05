import time
from barcode.decoder_cam import Leitor_codigo
from database.banco_de_dados import Database
from services.service import *


if __name__ == "__main__":
    Database.criar_banco()
    leitor = Leitor_codigo()
    ferr_service = FerramentaService()
    mat_service = MatriculaService()
    fer_repo = FerramentaRepository()
    mat_repo = MatriculaRepository()

    codigos_lidos = leitor.executar()

    for item in codigos_lidos:
        item_str = str(item)

        try:
            resultado = ferr_service.cadastrar(item, "Ferramenta")
            print(f"Código {item_str}: {resultado}")

            time.sleep(0.2)

            fer_info = fer_repo.buscar_por_codigo(item)
            if fer_info:
                print(f"Dados no banco: ID:{fer_info[0]} | Status:{fer_info[3]}")
        except Exception as e:
            print(f"Erro: {item_str}: {e}")

    matricula = input("Digite sua matricula: ")
    matricula_resultado = mat_service.remover(matricula)
    print(f"Matricula: {matricula}")

    time.sleep(0.1)

    mat_info = mat_repo.buscar_por_matricula(matricula)

    if mat_info:
        print(f"ID: {mat_info[0]}")
        print(f"Matrícula: {mat_info[1]}")
        print(f"Nome: {mat_info[2]}")
    else:
        print("Erro: Matrícula não encontrada no banco de dados.")
