from core.models import Enfermeira

def run():
    dados_enfermeiras = [
        (1, 'COREN1001', 'Ana Paula', '11999990001', None, 'ana.paula@email.com'),
        (2, 'COREN1002', 'Carlos Mendes', '11888881111', '11888882222', None),
        (3, 'COREN1003', 'Fernanda Alves', '11777770000', None, 'fernanda.alves@email.com'),
        (4, 'COREN1004', 'Marcos Dias', '11922223333', '11922224444', 'marcos.dias@email.com'),
        (5, 'COREN1005', 'Patrícia Gomes', '11955556666', None, None),
        (6, 'COREN1006', 'Roberto Costa', '11999991111', '11999992222', 'roberto.costa@email.com'),
        (7, 'COREN1007', 'Juliana Rocha', '11888883333', None, 'juliana.rocha@email.com'),
        (8, 'COREN1008', 'Bruno Moreira', '11777772222', '11777773333', None),
        (9, 'COREN1009', 'Larissa Costa', '11900001111', None, 'larissa.costa@email.com'),
        (10, 'COREN1010', 'Thiago Alves', '11955559999', '11955558888', 'thiago.alves@email.com'),
    ]

    for id_enf, coren, nome, tel1, tel2, email in dados_enfermeiras:
        if not Enfermeira.objects.filter(COREN=coren).exists():
            enfermeira = Enfermeira(
                id=id_enf,
                COREN=coren,
                nome=nome,
                telefone1=tel1,
                telefone2=tel2,
                email=email
            )
            enfermeira.save()
            print(f"Enfermeira {nome} criada com sucesso.")
        else:
            print(f"Enfermeira {nome} já existe.")