from core.models import Alergia, Paciente

def run():
    dados_alergias = [
        (1, 1, 'Alergia a Penicilina', 3, False, None),
        (2, 1, 'Alergia a Amoxicilina', 2, True, 0.02),
        (3, 1, 'Alergia a Pólen', 1, True, 0.10),
        (4, 3, 'Alergia a Amendoim', 4, False, None),
        (5, 5, 'Alergia a Látex', 2, True, 0.05),
        (6, 7, 'Alergia a Pólen', 1, True, 0.10),
        (7, 9, 'Alergia a Sulfa', 3, False, None),
    ]

    for id_alergia, id_paciente, nome, gravidade, tolerancia, dose_segura in dados_alergias:
        if not Alergia.objects.filter(id=id_alergia).exists():
            paciente = Paciente.objects.get(id=id_paciente)
            alergia = Alergia(
                id=id_alergia,
                paciente=paciente,
                nome=nome,
                gravidade=gravidade,
                tem_tolerancia_exposicao=tolerancia,
                dose_segura=dose_segura
            )
            alergia.save()
            print(f"Alergia '{nome}' criada para paciente {paciente.nome}.")
        else:
            print(f"Alergia '{nome}' para paciente {id_paciente} já existe.")