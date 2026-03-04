from database.repositories import FerramentaRepository
from interface.decoder_cam import Leitor_codigo
from database.banco_de_dados import Database

if __name__ == "__main__":

    teste = Leitor_codigo()
    busca = FerramentaRepository()
    con = Database.conectar()

    resultado = teste.executar()

    for item in resultado:

        ferramenta = busca.buscar_por_codigo(codigo=resultado)





