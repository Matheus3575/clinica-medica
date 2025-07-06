from django.contrib.auth.models import User
from core.models import Medico

def run():
    dados_medicos = [
        ('Dr. João Almeida', '12345', '11999990001', None, 'Cardiologia'),
        ('Dra. Maria Fernandes', '12346', '11999990002', '11999990003', 'Pediatria'),
        ('Dr. Carlos Silva', '12347', None, None, 'Ortopedia'),
        ('Dra. Ana Souza', '12348', '11888881111', None, 'Dermatologia'),
        ('Dr. Roberto Lima', '12349', '11922223333', '11922224444', 'Ginecologia'),
        ('Dra. Fernanda Costa', '12350', '11777772222', None, 'Neurologia'),
        ('Dr. Lucas Martins', '12351', '11955556666', '11955557777', 'Endocrinologia'),
        ('Dra. Juliana Rocha', '12352', None, '11900001111', 'Oftalmologia'),
        ('Dr. Pedro Carvalho', '12353', '11888889999', None, 'Psiquiatria'),
        ('Dra. Camila Dias', '12354', '11999993333', '11999994444', 'Urologia'),
        ('Dr. Ricardo Almeida', '12355', '11911112222', None, 'Radiologia'),
        ('Dra. Sandra Oliveira', '12356', '11822223333', '11822224444', 'Radiologia')
    ]

    for nome, crm, tel1, tel2, esp in dados_medicos:
        if not User.objects.filter(username=crm).exists():
            senha = 'senha' + crm[:3]
            user = User.objects.create_user(username=crm, password=senha)
            Medico.objects.create(
                nome=nome,
                CRM='CRM' + crm,
                telefone1=tel1,
                telefone2=tel2,
                especialidade=esp,
                user=user
            )
            print(f"{nome} criado com senha: {senha}")
        else:
            print(f"{nome} já existe.")