from repositories.repositories import  FerramentaRepository, MatriculaRepository, MovimentacaoRepository
from models.models import Matricula, Movimentacao
from datetime import datetime


class FerramentaService:

    def __init__(self):
        self.repo = FerramentaRepository()

    def cadastrar(self, codigo, descricao):

        if self.repo.buscar_por_codigo_ativo(codigo):
            return 1

        elif self.repo.buscar_por_codigo(codigo):
            return 2

        else:
            self.repo.salvar(codigo, descricao)
            return 3

    def remover(self, codigo):

        if not self.repo.buscar_por_codigo(codigo):
            return 1

        elif not self.repo.buscar_por_codigo_ativo(codigo):
            return 2

        else:
            self.repo.desativar(codigo)
            return 3

    def ativar(self, ferramenta):

        if not self.repo.buscar_por_codigo(ferramenta):
            return 1

        elif not self.repo.buscar_por_codigo_ativo(ferramenta):
            return 2

        else:
            self.repo.ativar(ferramenta)
            return 3

class MatriculaService:

    def __init__(self):
        self.repo = MatriculaRepository()

    def cadastrar(self, matricula_str, nome):

        if self.repo.buscar_por_matricula_ativo(matricula_str):
            return 1

        elif self.repo.buscar_por_matricula(matricula_str):
            return 2

        else:
            self.repo.salvar(matricula=matricula_str, nome=nome)
            return 3

    def atualizar(self, matricula_str, nome):

        if self.repo.buscar_por_matricula_ativo(matricula_str):
            self.repo.atualizar_nome(matricula_str, nome)
            return 1

        elif self.repo.buscar_por_matricula(matricula_str):
            return 2

        return None

    def remover(self, matricula_str):

        if not self.repo.buscar_por_matricula(matricula_str):
            return 1

        elif not self.repo.buscar_por_matricula_ativo(matricula_str):
            return 2

        else:
            self.repo.desativar(matricula_str)
            return 3

    def ativar(self, matricula_str):

        if not self.repo.buscar_por_matricula(matricula_str):
            return 1

        elif self.repo.buscar_por_matricula_ativo(matricula_str):
            return 2

        else:
            self.repo.ativar(matricula_str)
            return 3

    def buscar(self, matricula_str):

        if not self.repo.buscar_por_matricula(matricula_str):
            return 1

        else:
            id,matricula,nome,status = self.buscar(matricula_str)
            return id,matricula,nome,status


class MovimentacaoService:

    def __init__(self):
        self.movimentacao_repo = MovimentacaoRepository()
        self.ferramenta_repo = FerramentaRepository()
        self.matricula_repo = MatriculaRepository()

    def emprestar(self, ferramenta_codigo, matricula_codigo):

        m_reg = self.matricula_repo.buscar_por_matricula_ativo(matricula_codigo)
        if not m_reg:
            print("Matricula inexistente ou inativa")
            return None

        f_reg = self.ferramenta_repo.buscar_por_codigo_ativo(ferramenta_codigo)
        if not f_reg:
            print("Ferramenta inexistente ou inativa")
            return None

        ferramenta_id = f_reg[0]
        matricula_id = m_reg[0]

        # Verifica se já existe movimentação aberta
        if self.movimentacao_repo.buscar_movimentacao_aberta(ferramenta_id):
            print("Ferramenta já está emprestada.")
            return None

        data_retirada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        movimentacao = Movimentacao(
            ferramenta_id,
            matricula_id,
            data_retirada
        )

        self.movimentacao_repo.salvar(movimentacao)

        print("Empréstimo realizado com sucesso.")
        return None

    def devolver(self, matricula, ferramenta):

        m_reg = self.matricula_repo.buscar_por_matricula_ativo(matricula)
        if not m_reg:
            print("Matricula inexistente ou inativa")
            return None

        f_reg = self.ferramenta_repo.buscar_por_codigo_ativo(ferramenta)
        if not f_reg:
            print("Ferramenta inexistente ou inativa")
            return None

        ferramenta_id = f_reg[0]

        f_reg = self.movimentacao_repo.buscar_movimentacao_aberta(ferramenta_id)
        if not f_reg:
            print("Ferramenta não está emprestada.")
            return None

        data_devolucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.movimentacao_repo.registrar_devolucao(ferramenta_id, data_devolucao)
        return None
