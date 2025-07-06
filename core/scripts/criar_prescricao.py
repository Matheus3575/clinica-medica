from core.models import Prescricao, Consulta, Medicamento

def run():
    dados_prescricoes = [
        # (id_consulta, id_medicamento, dosagem, quantidade, duracao, periodicidade, necessita_alimentacao, horario_especifico)
        (1, 5, '50mg', 10, 30, '1x ao dia', False, '08:00:00'),
        (2, 2, '1g', 5, 5, '3x ao dia', True, '12:00:00'),
        (3, 25, '250mg', 7, 10, '2x ao dia', False, '08:00:00'),
        (4, 15, '300mg', 8, 7, '2x ao dia', True, '18:00:00'),
        (5, 16, '20mg', 12, 14, '1x ao dia', False, None),
        (6, 9, '2mg', 15, 20, '1x ao dia', False, '20:00:00'),
        (7, 7, '850mg', 20, 60, '2x ao dia', True, '07:00:00'),
        (8, 13, '10mg', 25, 7, '1x ao dia', False, None),
    ]

    for id_consulta, id_medicamento, dosagem, quantidade, duracao, periodicidade, necessita_alimentacao, horario in dados_prescricoes:
        if not Prescricao.objects.filter(consulta_id=id_consulta, medicamento_id=id_medicamento).exists():
            try:
                consulta = Consulta.objects.get(id=id_consulta)
                medicamento = Medicamento.objects.get(id=id_medicamento)
                Prescricao.objects.create(
                    consulta=consulta,
                    medicamento=medicamento,
                    dosagem=dosagem,
                    quantidade=quantidade,
                    duracao=duracao,
                    periodicidade=periodicidade,
                    necessita_alimentacao=necessita_alimentacao,
                    horario_especifico=horario
                )
                print(f"Prescrição criada: Consulta {id_consulta} - Medicamento {id_medicamento}")
            except Consulta.DoesNotExist:
                print(f"Consulta {id_consulta} não encontrada.")
            except Medicamento.DoesNotExist:
                print(f"Medicamento {id_medicamento} não encontrado.")
        else:
            print(f"Prescrição já existe: Consulta {id_consulta} - Medicamento {id_medicamento}")
