from .banco_de_dados import Database
from .service import FerramentaService, MatriculaService, MovimentacaoService


def main():

    # Criar banco (caso não exista)
    Database.criar_banco()

    # Instanciar serviços
    ferramenta_service = FerramentaService()
    matricula_service = MatriculaService()
    movimentacao_service = MovimentacaoService()

    # Teste simples
    print(ferramenta_service.cadastrar("F001", "Furadeira"))
    print(matricula_service.cadastrar("123", "Paulo"))

    print(movimentacao_service.emprestar("F001", "123"))
    print(movimentacao_service.devolver("F001"))


if __name__ == "__main__":
    main()
