from database.banco_de_dados import Database

class FerramentaRepository:

    def salvar(self, codigo, descricao):

            with Database.conectar() as con:
                con.execute("""
                    INSERT INTO ferramentas (codigo, descricao)
                    VALUES (?, ?)
                """, (codigo, descricao,))


    def buscar_por_codigo_ativo(self, codigo):

            with Database.conectar() as con:
                cursor = con.execute("""
                    SELECT id, codigo, descricao, status, ativo
                    FROM ferramentas
                    WHERE codigo = ? AND ativo = 1
                """, (codigo,))
                res = cursor.fetchone()
                if res:
                    return res


    def buscar_por_codigo(self, codigo):

            with Database.conectar() as con:
                cursor = con.execute("""
                    SELECT id, codigo, descricao, status, ativo
                    FROM ferramentas
                    WHERE codigo = ?
                """, (codigo,))
                res = cursor.fetchone()
                if res:
                    return res


    def atualizar_descricao(self, codigo, nova_descricao):

        with Database.conectar() as con:
            con.execute("""
                UPDATE ferramentas
                SET descricao = ?
                WHERE codigo = ?
            """, (nova_descricao, codigo))


    def desativar(self, codigo):

        with Database.conectar() as con:
            con.execute("""
                UPDATE ferramentas
                SET ativo = 0
                WHERE codigo = ?
            """, (codigo,))

    def ativar (self, codigo):

        with Database.conectar() as con:
            con.execute("""UPDATE ferramentas SET ativo = 1 WHERE codigo = ?""", (codigo,))


class MatriculaRepository:

    def salvar(self, matricula):

        with Database.conectar() as con:
            con.execute("""
                INSERT INTO matriculas (matricula, nome, ativo)
                VALUES (?, ?, ?)
            """, (matricula.matricula, matricula.nome, matricula.ativo))

    def buscar_por_matricula(self, matricula):

        with Database.conectar() as con:
            cursor = con.execute("""
                SELECT id, matricula, nome, ativo
                FROM matriculas
                WHERE matricula = ?
            """, (matricula,))
            busca = cursor.fetchone()
            return busca


    def buscar_por_matricula_ativo(self, matricula):
        with Database.conectar() as con:
            cursor = con.execute("""
                   SELECT id, matricula, nome, ativo
                   FROM matriculas
                   WHERE matricula = ? AND ativo = 1
               """, (matricula,))
            busca = cursor.fetchone()
            return busca


    def desativar(self, matricula):

        with Database.conectar() as con:
            con.execute("""UPDATE matriculas SET ativo = 0 WHERE matricula = ?""", (matricula,))

    def ativar(self, matricula):

        with Database.conectar() as con:
            con.execute("""UPDATE matriculas SET ativo = 1 WHERE matricula = ?""", (matricula,))


class MovimentacaoRepository:

    def salvar(self, movimentacao):

        with Database.conectar() as con:
            con.execute("""
                INSERT INTO movimentacoes 
                (ferramenta_id, matricula_id, data_retirada, data_devolucao)
                VALUES (?, ?, ?, ?)
            """, (
                movimentacao.ferramenta_id,
                movimentacao.matricula_id,
                movimentacao.data_retirada,
                movimentacao.data_devolucao
            ))

    def buscar_movimentacao_aberta(self, ferramenta_id):
        with Database.conectar() as con:
            cursor = con.execute("""
                SELECT id FROM movimentacoes
                WHERE ferramenta_id = ?
                AND data_devolucao IS NULL
            """, (ferramenta_id,))
            return cursor.fetchone()

    def registrar_devolucao(self, ferramenta_id, data_devolucao):
        with Database.conectar() as con:
            con.execute("""
                UPDATE movimentacoes
                SET data_devolucao = ?
                WHERE ferramenta_id = ?
                AND data_devolucao IS NULL
            """, (data_devolucao, ferramenta_id))
