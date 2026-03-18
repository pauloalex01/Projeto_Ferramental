import barcode
from barcode.writer import ImageWriter
import shutil
import os


def criar_codigo_barras(codigo):

    if len(str(codigo)) != 12:
        return "Código deve conter exatamente 12 dígitos numéricos"

    # Diretório base do projeto
    base_dir = os.path.dirname(os.path.abspath(__file__))

    pasta_destino = os.path.join(base_dir, "")
    os.makedirs(pasta_destino, exist_ok=True)

    # Criar código de barras
    codigo_de_barras = barcode.get('ean13', codigo, writer=ImageWriter())
    caminho_gerado = codigo_de_barras.save(os.path.join(base_dir, codigo))

    # Caminho final
    nome_arquivo = os.path.basename(caminho_gerado)
    caminho_final = os.path.join(pasta_destino, nome_arquivo)

    # Mover arquivo
    shutil.move(caminho_gerado, caminho_final)

    return f'Código de barras salvo em: {caminho_final}'


