from core.models import Ultrassom, Sala

def run():
    dados = [
        (1, 'UltraModel 1', 'UltraTech', '2024-02-15', 'Técnico A', 9),
        (2, 'UltraModel 2', 'UltraTech', '2023-12-01', 'Técnico B', 10)
    ]

    for id_ultrassom, modelo, fabricante, data_manutencao, responsavel, id_sala in dados:
        if not Ultrassom.objects.filter(id=id_ultrassom).exists():
            sala = Sala.objects.get(id=id_sala)
            Ultrassom.objects.create(
                id=id_ultrassom,
                modelo=modelo,
                fabricante=fabricante,
                data_manutencao=data_manutencao,
                responsavel_tecnico=responsavel,
                sala=sala
            )
            print(f"Ultrassom {modelo} criado com sucesso.")
        else:
            print(f"Ultrassom {modelo} já existe.")
