# Generated by Django 5.2.3 on 2025-07-06 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COREN', models.CharField(max_length=20, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone1', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=100)),
                ('estoque_minimo', models.IntegerField(default=50)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('validade', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('CRM', models.CharField(max_length=20, unique=True)),
                ('telefone1', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=20, null=True)),
                ('especialidade', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('bloco', models.CharField(max_length=10)),
                ('data_manutencao', models.DateField(blank=True, null=True)),
                ('capacidade', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('prontuario', models.CharField(db_index=True, max_length=50, unique=True)),
                ('acompanhante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='acompanha', to='core.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('CID11', models.CharField(max_length=10)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('forma_pagamento', models.CharField(blank=True, max_length=50, null=True)),
                ('consulta_descritiva', models.TextField(blank=True, null=True)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('gravidade', models.IntegerField()),
                ('tem_tolerancia_exposicao', models.BooleanField(default=False)),
                ('dose_segura', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Acolhimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pressao_arterial', models.CharField(blank=True, max_length=10, null=True)),
                ('temperatura', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('enfermeira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.enfermeira')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('data_manutencao', models.DateField(blank=True, null=True)),
                ('classificacao_risco', models.CharField(blank=True, max_length=50, null=True)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Ultrassom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=100)),
                ('data_manutencao', models.DateField(blank=True, null=True)),
                ('responsavel_tecnico', models.CharField(blank=True, max_length=100, null=True)),
                ('sala', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=100)),
                ('validade', models.DateField(blank=True, null=True)),
                ('dose_recomendada', models.IntegerField(blank=True, null=True)),
                ('nome', models.CharField(max_length=100)),
                ('acolhimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.acolhimento')),
            ],
        ),
        migrations.CreateModel(
            name='Prescricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosagem', models.CharField(max_length=50)),
                ('duracao', models.IntegerField()),
                ('periodicidade', models.CharField(max_length=50)),
                ('necessita_alimentacao', models.BooleanField(default=False)),
                ('horario_especifico', models.TimeField(blank=True, null=True)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.consulta')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medicamento')),
            ],
            options={
                'unique_together': {('consulta', 'medicamento')},
            },
        ),
    ]
