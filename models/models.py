
class Ferramenta:
    def __init__(self, codigo, descricao, status="Disponivel", ativo=1):
        self.codigo = codigo
        self.descricao = descricao
        self.status = status
        self.ativo = ativo


class Matricula:
    def __init__(self, matricula, nome, ativo=1):
        self.matricula = matricula
        self.nome = nome
        self.ativo = ativo


class Movimentacao:
    def __init__(self, ferramenta_id, matricula_id, quantidade, data_retirada, data_devolucao=None):
        self.ferramenta_id = ferramenta_id
        self.matricula_id = matricula_id
        self.data_retirada = data_retirada
        self.data_devolucao = data_devolucao
        self.quantidade = quantidade

    def esta_aberta(self):
        return self.data_devolucao is None