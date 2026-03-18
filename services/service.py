from repositories.repositories import  FerramentaRepository, MatriculaRepository, MovimentacaoRepository
from models.models import Movimentacao
from datetime import datetime


class FerramentaService:

    def __init__(self):
        self.repo = FerramentaRepository()

    def cadastrar(self, codigo, descricao, quantidade):

        if self.repo.buscar_por_codigo_ativo(codigo):
            return 1

        elif self.repo.buscar_por_codigo(codigo):
            return 2

        else:
            self.repo.salvar(codigo=codigo, descricao=descricao, quantidade=quantidade)
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

        elif self.repo.buscar_por_codigo_ativo(ferramenta):
            return 2

        else:
            self.repo.ativar(ferramenta)
            return 3

    def buscar(self, ferramenta):

        if not self.repo.buscar_por_codigo(ferramenta):
            return 1

        else:
            busca = self.repo.buscar_por_codigo(ferramenta)
            return busca

    def buscar_quantidade(self, ferramenta):

        if not self.repo.buscar_por_codigo(ferramenta):
            return 1

        else:
            identificao, codigo, descricao, status, quantidade, ativo,  = self.repo.buscar_por_codigo(ferramenta)
            return quantidade

    def atualizar(self, ferramenta_codigo, descricao):

        if self.repo.buscar_por_codigo_ativo(ferramenta_codigo):
            self.repo.atualizar_descricao(codigo=ferramenta_codigo, nova_descricao=descricao)
            return 0

        elif self.repo.buscar_por_codigo(codigo=ferramenta_codigo):
            return 1

        elif not self.repo.buscar_por_codigo(codigo=ferramenta_codigo):
            return 2

        return None


class MatriculaService:

    def __init__(self):
        self.repo = MatriculaRepository()

    def cadastrar(self, matricula_str, nome, setor):

        if self.repo.buscar_por_matricula_ativo(matricula_str):
            return 1

        elif self.repo.buscar_por_matricula(matricula_str):
            return 2

        else:
            self.repo.salvar(matricula=matricula_str, nome=nome, setor=setor)
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
            busca = self.repo.buscar_por_matricula(matricula_str)
            return busca


class MovimentacaoService:

    def __init__(self):
        self.movimentacao_repo = MovimentacaoRepository()
        self.ferramenta_repo = FerramentaRepository()
        self.matricula_repo = MatriculaRepository()


    def buscar_matricula_id(self, matricula):

        m_reg = self.matricula_repo.buscar_por_matricula_ativo(matricula)
        if not m_reg:
            return False
        m_reg = m_reg[0]
        return m_reg

    def buscar_ferramenta_id(self, ferramenta):

        f_reg = self.ferramenta_repo.buscar_por_codigo_ativo(ferramenta)
        if not f_reg:
            return False
        f_reg = f_reg[0]
        return f_reg

    def emprestar(self, ferramenta_codigo, matricula_codigo, quantidade):

        matricula_id = self.buscar_matricula_id(matricula_codigo)

        if not matricula_id:
            return 1

        ferramenta_id = self.buscar_ferramenta_id(ferramenta_codigo)

        if not ferramenta_id:
            return 2

        quantidade = self.ferramenta_repo.buscar_por_quantidade(ferramenta_id)

        if quantidade <= 0:
            return 5  # sem ferramenta disponível

        if self.movimentacao_repo.buscar_movimentacao_aberta_ferramenta(ferramenta_id):
            return 3

        data_retirada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        movimentacao = Movimentacao(
            ferramenta_id,
            matricula_id,
            data_retirada
        )

        self.movimentacao_repo.salvar(movimentacao)


        self.ferramenta_repo.diminuir_quantidade(ferramenta_id)

        return 4

    def devolver(self, ferramenta, matricula):

        matricula_id = self.buscar_matricula_id(matricula)

        if not matricula_id:
            return 1

        ferramenta_id = self.buscar_ferramenta_id(ferramenta)

        if not ferramenta_id:
            return 2

        f_reg = self.movimentacao_repo.buscar_movimentacao_aberta_ferramenta(ferramenta_id)

        if not f_reg:
            return 3

        data_devolucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.movimentacao_repo.registrar_devolucao(ferramenta_id, data_devolucao)

        self.ferramenta_repo.aumentar_quantidade(ferramenta_id)

        return 4

    def buscar_movimentacoes_abertas_matricula(self, matricula_codigo):

        matricula_id = self.buscar_matricula_id(matricula_codigo)

        if not matricula_id:
            return 1

        busca = self.movimentacao_repo.buscar_movimentacao_aberta_matricula(matricula_id)

        return busca

    def buscar_movimentacoes_abertas_ferramenta(self, ferramenta_codigo):

        ferramenta_id = self.buscar_ferramenta_id(ferramenta_codigo)

        if not ferramenta_id:
            return 1

        busca = self.movimentacao_repo.buscar_movimentacao_aberta_ferramenta(ferramenta_id)

        return busca

    def carregar_historico(self):

        historico = self.movimentacao_repo.carregar_historico()

        if not historico:
            return []

        return historico
