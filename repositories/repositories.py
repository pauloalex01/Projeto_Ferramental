from database.banco_de_dados import Database

class FerramentaRepository:

    def salvar(self, codigo, descricao, quantidade):

            with Database.conectar() as con:
                con.execute("""
                    INSERT INTO ferramentas (codigo, descricao, quantidade)
                    VALUES (?, ?)
                """, (codigo, descricao,quantidade,))


    def buscar_por_codigo_ativo(self, codigo):

            with Database.conectar() as con:
                cursor = con.execute("""
                    SELECT id, codigo, descricao, status, quantidade, ativo
                    FROM ferramentas
                    WHERE codigo = ? AND ativo = 1
                """, (codigo,))
                res = cursor.fetchone()
                if res:
                    return res
            return None

    def buscar_por_codigo(self, codigo):

            with Database.conectar() as con:
                cursor = con.execute("""
                    SELECT id, codigo, descricao, status, quantidade, ativo
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

    def atualizar_quantidade(self, codigo, nova_quantidade):

        with Database.conectar() as con:
            con.execute("""
                UPDATE ferramentas
                SET quantidade = ?
                WHERE codigo = ?
            """, (nova_quantidade, codigo))


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

    def diminuir_quantidade(self, ferramenta_id):

        with Database.conectar() as con:
            cursor = con.cursor()
            cursor.execute("""
            UPDATE ferramentas
            SET quantidade = quantidade - 1
            WHERE id = ? AND quantidade > 0
            """, (ferramenta_id,))

    def aumentar_quantidade(self, ferramenta_id):

        with Database.conectar() as con:
            cursor = con.cursor()
            cursor.execute("""
            UPDATE ferramentas
            SET quantidade = quantidade + 1
            WHERE id = ? AND quantidade > 0
            """, (ferramenta_id,))


class MatriculaRepository:

    def salvar(self, matricula, nome, setor):

        with Database.conectar() as con:
            con.execute("""
                INSERT INTO matriculas (matricula, nome, setor)
                VALUES (?, ?, ?)
            """, (matricula, nome, setor,))

    def buscar_por_matricula(self, matricula):

        with Database.conectar() as con:
            cursor = con.execute("""
                SELECT id, matricula, nome, ativo, setor
                FROM matriculas
                WHERE matricula = ?
            """, (matricula,))
            busca = cursor.fetchone()
            return busca


    def buscar_por_matricula_ativo(self, matricula):
        with Database.conectar() as con:
            cursor = con.execute("""
                   SELECT id, matricula, nome, ativo, setor
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


    def atualizar_nome(self, matricula, nome):

        with Database.conectar() as con:
            con.execute("""
                UPDATE matriculas
                SET nome = ?
                WHERE matricula = ?
            """, (matricula, nome))

    def atualizar_setor(self, matricula, setor):
        with Database.conectar() as con:
            con.execute("""
                   UPDATE matriculas
                   SET setor = ?
                   WHERE matricula = ?
               """, (matricula, setor))

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

    def buscar_movimentacao_aberta_ferramenta(self, ferramenta_id):
        with Database.conectar() as con:
            cursor = con.execute("""
                SELECT * FROM movimentacoes
                WHERE ferramenta_id = ?
                AND data_devolucao IS NULL
            """, (ferramenta_id,))
            return cursor.fetchone()

    def buscar_movimentacao_aberta_matricula(self, matricula_id):
        with Database.conectar() as con:
            cursor = con.execute("""
                SELECT * FROM movimentacoes
                WHERE matricula_id = ?
                AND data_devolucao IS NULL
            """, (matricula_id,))
            return cursor.fetchone()


    def registrar_devolucao(self, ferramenta_id, data_devolucao):
        with Database.conectar() as con:
            con.execute("""
                UPDATE movimentacoes
                SET data_devolucao = ?
                WHERE ferramenta_id = ?
                AND data_devolucao IS NULL
            """, (data_devolucao, ferramenta_id))

