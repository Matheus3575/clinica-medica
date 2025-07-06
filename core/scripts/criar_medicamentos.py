from core.models import Medicamento

def run():
    dados_medicamentos = [
         (1, 'Paracetamol 500mg', 'Farmaceutica A', 75, 10.00, '2025-12-31'),
        (2, 'Dipirona 1g', 'Farmaceutica B', 60, 15.00, '2024-11-30'),
        (3, 'Ibuprofeno 400mg', 'Farmaceutica C', 120, 12.00, '2025-06-30'),
        (4, 'AAS 100mg', 'Farmaceutica D', 90, 8.50, '2025-08-31'),
        (5, 'Losartana 50mg', 'Farmaceutica E', 55, 35.00, '2026-01-31'),
        (6, 'Metformina 850mg', 'Farmaceutica F', 110, 25.00, '2025-05-31'),
        (7, 'Glimepirida 2mg', 'Farmaceutica G', 70, 40.00, '2025-09-30'),
        (8, 'Loratadina 10mg', 'Farmaceutica H', 80, 18.00, '2024-12-31'),
        (9, 'Clonazepam 2mg', 'Farmaceutica I', 65, 50.00, '2025-07-31'),
        (10, 'Ranitidina 150mg', 'Farmaceutica J', 100, 22.00, '2024-10-31'),
        (11, 'Amiodarona 200mg', 'Farmaceutica K', 85, 55.00, '2025-03-31'),
        (12, 'Captopril 25mg', 'Farmaceutica L', 95, 30.00, '2025-04-30'),
        (13, 'Cetirizina 10mg', 'Farmaceutica M', 72, 20.00, '2026-02-28'),
        (14, 'Omeprazol 20mg', 'Farmaceutica N', 58, 28.00, '2025-11-30'),
        (15, 'Clindamicina 300mg', 'Farmaceutica O', 105, 45.00, '2025-09-30'),
        (16, 'Prednisona 20mg', 'Farmaceutica P', 68, 27.00, '2025-12-31'),
        (17, 'Dexametasona 4mg', 'Farmaceutica Q', 62, 32.00, '2026-01-31'),
        (18, 'Salbutamol 100mcg', 'Farmaceutica R', 77, 24.00, '2025-05-31'),
        (19, 'Levotiroxina 50mcg', 'Farmaceutica S', 66, 33.00, '2025-08-31'),
        (20, 'Nifedipino 30mg', 'Farmaceutica T', 59, 37.00, '2026-03-31'),
        (21, 'Omeprazol 40mg', 'Farmaceutica U', 88, 30.00, '2026-02-28'),
        (22, 'Ranitidina 300mg', 'Farmaceutica V', 95, 25.00, '2025-07-31'),
        (23, 'Fluconazol 150mg', 'Farmaceutica W', 85, 50.00, '2025-11-30'),
        (24, 'Dipropionato de Betametasona 0,05%', 'Farmaceutica X', 78, 30.00, '2025-10-31'),
        (25, 'Naproxeno 250mg', 'Farmaceutica Y', 90, 19.00, '2025-09-30'),
        (26, 'Cetoconazol 200mg', 'Farmaceutica Z', 69, 44.00, '2026-01-31'),
        (27, 'Morfofina 10mg', 'Farmaceutica AA', 100, 65.00, '2025-06-30'),
        (28, 'Glimepirida 2mg', 'Farmaceutica BB', 55, 42.00, '2025-12-31'),
        (29, 'Clopidogrel 75mg', 'Farmaceutica CC', 61, 70.00, '2026-04-30'),
        (30, 'Ibuprofeno 600mg', 'Farmaceutica DD', 73, 20.00, '2025-08-31'),
    ]

    for id_medicamento, nome, fabricante, estoque_minimo, preco, validade in dados_medicamentos:
        if not Medicamento.objects.filter(id=id_medicamento).exists():
            Medicamento.objects.create(
                id=id_medicamento,
                nome=nome,
                fabricante=fabricante,
                estoque_minimo=estoque_minimo,
                preco=preco,
                validade=validade
            )
            print(f"Medicamento '{nome}' criado.")
        else:
            print(f"Medicamento '{nome}' já existe.")