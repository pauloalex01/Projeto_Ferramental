from .repositories import  FerramentaRepository, MatriculaRepository, MovimentacaoRepository
from .models import Ferramenta, Matricula, Movimentacao
from datetime import datetime


class FerramentaService:

    def __init__(self):
        self.repo = FerramentaRepository()

    def cadastrar(self, codigo, descricao):

        if self.repo.buscar_por_codigo(codigo):
            return "Ferramenta já cadastrada."

        self.repo.salvar(codigo, descricao)
        return "Ferramenta cadastrada com sucesso."

    def remover(self, codigo):

        if not self.repo.buscar_por_codigo(codigo):
            return "Ferramenta não encontrada."

        self.repo.desativar(codigo)
        return "Ferramenta desativada com sucesso."


class MatriculaService:

    def __init__(self):
        self.repo = MatriculaRepository()

    def cadastrar(self, matricula_str, nome):

        if self.repo.buscar_por_matricula(matricula_str):
            return "Matrícula já cadastrada."

        nova_matricula = Matricula(matricula_str, nome)
        self.repo.salvar(nova_matricula)
        return "Matricula cadastrada com sucesso."

    def remover(self, matricula_str):

        if not self.repo.buscar_por_matricula(matricula_str):
            return "Matricula não encontrada."

        self.repo.desativar(matricula_str)
        return "Matricula desativada com sucesso."


class MovimentacaoService:

    def __init__(self):
        self.movimentacao_repo = MovimentacaoRepository()
        self.ferramenta_repo = FerramentaRepository()
        self.matricula_repo = MatriculaRepository()

    def emprestar(self, ferramenta_codigo, matricula_codigo):

        f_reg = self.ferramenta_repo.buscar_por_codigo(ferramenta_codigo)
        if not f_reg:
            return "Ferramenta inexistente ou inativa"

        m_reg = self.matricula_repo.buscar_por_matricula(matricula_codigo)
        if not m_reg:
            return "Matricula inexistente ou inativa"

        ferramenta_id = f_reg[0]
        matricula_id = m_reg[0]

        # Verifica se já existe movimentação aberta
        if self.movimentacao_repo.buscar_movimentacao_aberta(ferramenta_id):
            return "Ferramenta já está emprestada."

        data_retirada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        movimentacao = Movimentacao(
            ferramenta_id,
            matricula_id,
            data_retirada
        )

        self.movimentacao_repo.salvar(movimentacao)

        return "Empréstimo realizado com sucesso."

    def devolver(self, ferramenta_id):

        f_reg = self.movimentacao_repo.buscar_movimentacao_aberta(ferramenta_id)
        if not f_reg:
            return "Ferramenta não está emprestada."

        data_devolucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.movimentacao_repo.registrar_devolucao(ferramenta_id, data_devolucao)

        return "Devolução registrada com sucesso."
