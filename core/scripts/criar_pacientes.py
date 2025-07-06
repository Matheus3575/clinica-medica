from core.models import Paciente
from django.utils.dateparse import parse_date

def run():
    dados_pacientes = [
        (1, 'Maria Silva', '1985-05-12', '11999998888', None, 'maria.silva@email.com', None),
        (2, 'João Souza', '1990-10-30', '11888887777', '11999991111', 'joao.souza@email.com', 1),
        (3, 'Ana Pereira', '1978-07-19', '11944443333', None, 'ana.pereira@email.com', None),
        (4, 'Carlos Lima', '1982-11-23', '1177776666', '11922223333', 'carlos.lima@email.com', 3),
        (5, 'Patrícia Gomes', '1995-02-14', '11888889999', None, None, None),
        (6, 'Roberto Costa', '1988-09-07', '11955554444', '11955556666', 'roberto.costa@email.com', 5),
        (7, 'Fernanda Alves', '1993-12-01', '11777779999', None, 'fernanda.alves@email.com', None),
        (8, 'Rafael Martins', '1980-05-18', '11922221111', '11933334444', 'rafael.martins@email.com', 7),
        (9, 'Juliana Rocha', '1975-03-27', '11888884444', None, 'juliana.rocha@email.com', None),
        (10, 'Marcos Dias', '1987-06-10', '11999990000', '11900001111', None, 9),
        (11, 'Carla Fernandes', '1991-01-15', '11777770000', None, 'carla.fernandes@email.com', None),
        (12, 'Bruno Moreira', '1983-04-20', '11955557777', '11955558888', 'bruno.moreira@email.com', None),
        (13, 'Simone Nunes', '1979-08-08', '11888882222', None, None, None),
        (14, 'Lucas Melo', '1994-11-29', '11922220000', '11922229999', 'lucas.melo@email.com', None),
        (15, 'Aline Rocha', '1986-07-07', '11777770001', None, 'aline.rocha@email.com', None),
        (16, 'Pedro Albuquerque', '1981-10-16', '11999995555', '11999996666', 'pedro.albuquerque@email.com', None),
        (17, 'Natália Silva', '1992-03-05', '11888881111', None, 'natalia.silva@email.com', None),
        (18, 'Felipe Castro', '1984-09-22', '11955552222', '11955553333', None, None),
        (19, 'Larissa Costa', '1989-05-30', '11777773333', None, 'larissa.costa@email.com', None),
        (20, 'Thiago Alves', '1990-12-12', '11922221112', '11922221113', 'thiago.alves@email.com', None),
        (21, 'Renata Lima', '1987-01-01', '11999991111', None, 'renata.lima@email.com', None),
        (22, 'Gustavo Fernandes', '1985-03-19', '11888883333', '11888884444', None, None),
        (23, 'Marcela Vieira', '1993-07-25', '11955559999', None, 'marcela.vieira@email.com', None),
        (24, 'Eduardo Rocha', '1976-11-11', '11777771111', '11777772222', 'eduardo.rocha@email.com', None),
        (25, 'Vanessa Almeida', '1982-02-28', '11922223333', None, None, None),
        (26, 'Rogério Martins', '1980-08-15', '11999992222', '11999993333', 'rogerio.martins@email.com', None),
        (27, 'Amanda Souza', '1991-06-17', '11888884444', None, 'amanda.souza@email.com', None),
        (28, 'Felipe Santos', '1983-09-09', '11955554444', '11955556666', None, None),
        (29, 'Bianca Lopes', '1995-04-21', '11777770002', None, 'bianca.lopes@email.com', None),
        (30, 'Diego Fernandes', '1988-12-03', '11922220001', '11922220002', 'diego.fernandes@email.com', None),
	(31, 'João Nunes da Silva', '1950-12-03', '11922660001', '11976220002', 'joao.nunes@email.com', None),
    ]
    

    for id_paciente, nome, data_nasc, tel1, tel2, email, id_acompanhante in dados_pacientes:
        # Verifica se já existe (evita duplicados)
        if not Paciente.objects.filter(prontuario=f"PRONT{id_paciente:03d}").exists():
            paciente = Paciente(
                id=id_paciente,
                nome=nome,
                data_nascimento=parse_date(data_nasc),
                telefone=tel1,
                telefone2=tel2,
                email=email,
                acompanhante_id=id_acompanhante
            )
            # O prontuario será criado automaticamente no save se não passado
            paciente.prontuario = f"PRONT{id_paciente:03d}"  # garante prontuario fixo igual ao seu INSERT
            paciente.save()
            print(f"Paciente {nome} criado com sucesso.")
        else:
            print(f"Paciente {nome} já existe.")