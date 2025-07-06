from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, null=True, blank=True)
    telefone2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    prontuario = models.CharField(max_length=50, unique=True, db_index=True)
    acompanhante = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='acompanha')

    def save(self, *args, **kwargs):
        if not self.prontuario:
            ultimo = Paciente.objects.order_by('-id').first()
            if ultimo and ultimo.prontuario.startswith("PRONT"):
                numero = int(ultimo.prontuario.replace("PRONT", ""))
            else:
                numero = 0
            self.prontuario = f"PRONT{numero + 1:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Enfermeira(models.Model):
    COREN = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    telefone1 = models.CharField(max_length=20, null=True, blank=True)
    telefone2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome


class Acolhimento(models.Model):
    enfermeira = models.ForeignKey(Enfermeira, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    pressao_arterial = models.CharField(max_length=10, null=True, blank=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)


class Vacina(models.Model):
    acolhimento = models.ForeignKey(Acolhimento, on_delete=models.CASCADE)
    fabricante = models.CharField(max_length=100)
    validade = models.DateField(null=True, blank=True)
    dose_recomendada = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    CRM = models.CharField(max_length=20, unique=True)
    telefone1 = models.CharField(max_length=20, null=True, blank=True)
    telefone2 = models.CharField(max_length=20, null=True, blank=True)
    especialidade = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.CRM})"


class Sala(models.Model):
    numero = models.IntegerField()
    bloco = models.CharField(max_length=10)
    data_manutencao = models.DateField(null=True, blank=True)
    capacidade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Sala {self.numero} - Bloco {self.bloco}"


class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    CID11 = models.CharField(max_length=10, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    forma_pagamento = models.CharField(max_length=50, null=True, blank=True)

    consulta_descritiva = models.TextField(null=True, blank=True)  # ADICIONADO

    def __str__(self):
          return f"{self.paciente.nome} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

    def clean(self):
        from datetime import timedelta
        from django.core.exceptions import ValidationError
        
        margem = timedelta(minutes=30)
        inicio = self.data_hora - margem
        fim = self.data_hora + margem

        conflito = Consulta.objects.filter(
            medico=self.medico,
            data_hora__range=(inicio, fim)
        ).exclude(id=self.id).exists()

        if conflito:
            raise ValidationError("Já existe uma consulta agendada para esse médico em horário próximo.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class Alergia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    gravidade = models.IntegerField()
    tem_tolerancia_exposicao = models.BooleanField(default=False)
    dose_segura = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    estoque_minimo = models.IntegerField(default=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Prescricao(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosagem = models.CharField(max_length=50)
    duracao = models.IntegerField()
    periodicidade = models.CharField(max_length=50)
    necessita_alimentacao = models.BooleanField(default=False)
    horario_especifico = models.TimeField(null=True, blank=True)
    quantidade = models.IntegerField(default=1)  

    class Meta:
        unique_together = (('consulta', 'medicamento'),)

class Equipamento(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    data_manutencao = models.DateField(null=True, blank=True)
    classificacao_risco = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome


class Ultrassom(models.Model):
    modelo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    data_manutencao = models.DateField(null=True, blank=True)
    responsavel_tecnico = models.CharField(max_length=100, null=True, blank=True)
    sala = models.OneToOneField(Sala, on_delete=models.CASCADE)  # relacionamento 1:1

    def __str__(self):
        return self.modelo