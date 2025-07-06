from core.models import Vacina, Acolhimento
from datetime import datetime

def run():
    dados_vacinas = [
        (1, 1, 'Fabricante A', '2025-12-31', 2, 'Vacina Hepatite B'),
        (2, 4, 'Fabricante D', '2025-08-31', 2, 'Vacina HPV'),
    ]

    for id_vac, acolh_id, fab, validade, dose, nome in dados_vacinas:
        if not Vacina.objects.filter(id=id_vac).exists():
            acolhimento = Acolhimento.objects.get(id=acolh_id)
            vacina = Vacina(
                id=id_vac,
                acolhimento=acolhimento,
                fabricante=fab,
                dose_recomendada=dose,
                nome=nome
            )
            if validade:
                vacina.validade = datetime.strptime(validade, "%Y-%m-%d").date()
            vacina.save()
            print(f"Vacina {nome} criada para acolhimento {acolh_id}.")
        else:
            print(f"Vacina {nome} para acolhimento {acolh_id} já existe.")