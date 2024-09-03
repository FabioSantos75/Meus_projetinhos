import shutil
import os
import time
from datetime import datetime


def criar_backup(origem, destino):
    # Verifica se a pasta de origem existe
    if not os.path.exists(origem):
        print(f"A pasta de origem '{origem}' não existe.")
        return

    # Cria o nome da pasta de backup com a data e hora
    data_hora = datetime.now().strftime('%Y%m%d_%H%M%S')
    destino_completo = os.path.join(destino, f'backup_{data_hora}')

    try:
        # Copia o conteúdo da pasta de origem para a pasta de destino ('shutil.move' para mover)
        shutil.copytree(origem, destino_completo)
        print(f'Backup criado com sucesso em: {destino_completo}')
    except Exception as e:
        print(f'Erro ao criar o backup: {e}')


def backup_automatico(origem, destino, intervalo_segundos):
    while True:
        criar_backup(origem, destino)
        time.sleep(intervalo_segundos)


if __name__ == "__main__":
    # Defina os caminhos da pasta de origem e destino
    pasta_origem = r'C:\Users\fabio\OneDrive\Documentos\TESTE\origm'
    pasta_destino = r'C:\Users\fabio\OneDrive\Documentos\TESTE\DESTINO'


    intervalo = 3600



    backup_automatico(pasta_origem, pasta_destino, intervalo)



