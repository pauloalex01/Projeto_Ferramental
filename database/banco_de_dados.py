import sqlite3

class Database:

    DB_PATH = 'controle_ferramental.sqlite'

    @staticmethod
    def conectar():
        con = sqlite3.connect(Database.DB_PATH, timeout=5)
        con.execute("PRAGMA foreign_keys = 1")
        return con

    @staticmethod
    def criar_banco():

        with Database.conectar() as con:
            cursor = con.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ferramentas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL UNIQUE,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Disponivel',
            ativo INTEGER DEFAULT 1
            )
            """)

            # Tabela Matriculas
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS matriculas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            matricula TEXT NOT NULL UNIQUE,
            nome TEXT NOT NULL,
            ativo INTEGER DEFAULT 1
            )
            """)

            # Tabela Movimentações
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ferramenta_id INTEGER NOT NULL,
            matricula_id INTEGER NOT NULL,
            data_retirada TEXT NOT NULL,
            data_devolucao TEXT,
            FOREIGN KEY (ferramenta_id) REFERENCES ferramentas(id),
            FOREIGN KEY (matricula_id) REFERENCES matriculas(id)
            )
            """)

        print("Banco criado com sucesso")
