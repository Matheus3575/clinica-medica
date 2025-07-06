from core.models import Sala
from datetime import datetime

def run():
    dados_salas = [
        (1, 101, 'A', '2024-01-15', 20),
        (2, 102, 'A', None, 15),
        (3, 201, 'B', '2023-12-10', 30),
        (4, 202, 'B', None, None),
        (5, 301, 'C', '2024-02-20', 25),
        (6, 302, 'C', '2023-11-05', None),
        (7, 401, 'D', None, 18),
        (8, 402, 'D', '2024-03-12', 22),
        (9, 501, 'E', None, None),
        (10, 502, 'E', '2023-10-30', 16),
    ]

    for id_sala, numero, bloco, data_man, capacidade in dados_salas:
        if not Sala.objects.filter(id=id_sala).exists():
            sala = Sala(
                id=id_sala,
                numero=numero,
                bloco=bloco,
                capacidade=capacidade
            )
            if data_man:
                sala.data_manutencao = datetime.strptime(data_man, "%Y-%m-%d").date()
            sala.save()
            print(f"Sala {numero} - Bloco {bloco} criada com sucesso.")
        else:
            print(f"Sala {numero} - Bloco {bloco} já existe.")