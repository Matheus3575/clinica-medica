from core.models import Consulta, Medico, Paciente, Sala
from django.utils.dateparse import parse_datetime

def run():
    dados_consultas = [
        # (id, id_medico, id_paciente, id_sala, data_hora, CID11, valor, forma_pagamento, consulta_descritiva)
        (1, 1, 1, 1, '2024-06-05 10:00:00', 'I10', 150.00, 'Cartão', 'Paciente hipertenso, relata dor torácica leve. PA alta, sem sinais de urgência.'),
        (2, 2, 2, 2, '2024-06-05 11:30:00', 'J45', 200.00, 'Dinheiro', 'Asma com tosse seca e chiado. Prescrito broncodilatador.'),
        (3, 3, 3, 3, '2024-06-06 08:45:00', 'M16', 180.00, 'Cartão', 'Dor no joelho direito, quadro crônico, sem trauma recente.'),
        (4, 4, 4, 4, '2024-06-06 09:15:00', 'L20', 160.00, 'Convênio', 'Dermatite atópica ativa com placas pruriginosas. Prescrito corticosteroide tópico.'),
        (5, 5, 5, 5, '2024-06-07 14:00:00', 'N93', 210.00, 'Cartão', 'Dor pélvica e sangramento irregular. Solicitada ultrassonografia.'),
        (6, 6, 6, 6, '2024-06-07 15:30:00', 'G40', 190.00, 'Dinheiro', 'Crises convulsivas recentes, iniciada medicação anticonvulsivante.'),
        (7, 7, 7, 7, '2024-06-08 13:00:00', 'E11', 170.00, 'Convênio', 'Diabetes tipo 2 com controle instável, solicitados exames.'),
        (8, 8, 8, 8, '2024-06-08 14:30:00', 'H25', 220.00, 'Cartão', 'Visão reduzida progressiva, suspeita de glaucoma, iniciado tratamento.')
    ]

    for (id_consulta, id_medico, id_paciente, id_sala, data_hora_str, cid11, valor, pagamento, desc) in dados_consultas:
        if not Consulta.objects.filter(id=id_consulta).exists():
            medico = Medico.objects.get(id=id_medico)
            paciente = Paciente.objects.get(id=id_paciente)
            sala = Sala.objects.get(id=id_sala)
            data_hora = parse_datetime(data_hora_str)

            Consulta.objects.create(
                id=id_consulta,
                medico=medico,
                paciente=paciente,
                sala=sala,
                data_hora=data_hora,
                CID11=cid11,
                valor=valor,
                forma_pagamento=pagamento,
                consulta_descritiva=desc
            )
            print(f"Consulta {id_consulta} criada.")
        else:
            print(f"Consulta {id_consulta} já existe.")