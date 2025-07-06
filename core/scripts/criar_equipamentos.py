from core.models import Equipamento, Sala
from datetime import datetime

def run():
    dados_equipamentos = [
        (1, 1, 'Esfigmomanômetro', 'Modelo X', '2024-01-15', 'Baixo'),
        (2, 1, 'Balança', 'Modelo Y', '2023-12-10', 'Baixo'),
        (3, 1, 'Termômetro', 'EnferModel 1', '2023-11-05', 'Baixo'),
        (4, 1, 'Esfigmomanômetro', 'EnferModel 2', '2024-01-10', 'Baixo'),
        (5, 3, 'Espéculo', 'GyneModel 1', '2024-02-20', 'Baixo'),
        (6, 3, 'Colposcópio', 'GyneModel 2', '2023-11-05', 'Médio'),
        (7, 4, 'Oftalmoscópio', 'NeuroModel 1', '2023-11-05', 'Baixo'),
        (8, 4, 'Diapasão', 'NeuroModel 2', '2024-01-01', 'Baixo'),
        (9, 5, 'Bisturi', 'DermaModel 1', '2023-10-30', 'Alto'),
        (10, 5, 'Materiais Cirúrgicos', 'DermaKit 3', '2024-02-15', 'Alto'),
    ]

    for id_eq, sala_id, nome, modelo, data_man, risco in dados_equipamentos:
        if not Equipamento.objects.filter(id=id_eq).exists():
            sala = Sala.objects.get(id=sala_id)
            equipamento = Equipamento(
                id=id_eq,
                sala=sala,
                nome=nome,
                modelo=modelo,
                classificacao_risco=risco
            )
            if data_man:
                equipamento.data_manutencao = datetime.strptime(data_man, "%Y-%m-%d").date()
            equipamento.save()
            print(f"Equipamento {nome} criado na sala {sala.numero}.")
        else:
            print(f"Equipamento {nome} na sala {sala.numero} já existe.")