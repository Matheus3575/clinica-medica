from django import forms
from django.core.exceptions import ValidationError
from .models import Consulta, Paciente, Sala, Medicamento,Prescricao


class AgendarConsultaForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), label='Paciente')
    sala = forms.ModelChoiceField(queryset=Sala.objects.all(), label='Sala')
    data_hora = forms.DateTimeField(
        label='Data e Hora da Consulta',
        input_formats=['%Y-%m-%dT%H:%M'],  # para o datetime-local funcionar
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sala'].label_from_instance = lambda obj: f"Sala {obj.numero}"

    def clean(self):
        cleaned_data = super().clean()
        paciente = cleaned_data.get('paciente')
        sala = cleaned_data.get('sala')
        data_hora = cleaned_data.get('data_hora')

        if sala and data_hora:
            # Verificar se já existe uma consulta marcada para a mesma sala no mesmo horário
            if Consulta.objects.filter(sala=sala, data_hora=data_hora).exists():
                raise ValidationError("Já existe uma consulta agendada para essa sala neste horário.")

        return cleaned_data

from django import forms

class FinalizarConsultaForm(forms.Form):
    consulta_descritiva = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 30,
            'style': 'resize: vertical; width: 100%; font-family: inherit; font-size: 1.1rem; padding: 1rem; border-radius: 6px; border: 2px solid #1d72b8; outline-offset: 2px; outline-color: transparent; transition: outline-color 0.3s ease;'
        }),
        required=False,
        label="Descrição da Consulta"
    )

class PrescricaoForm(forms.Form):
    medicamento = forms.ModelChoiceField(
        queryset=Medicamento.objects.all().order_by('preco'),
        label='Medicamento',
        widget=forms.Select()
    )
    dosagem = forms.CharField(max_length=50)
    duracao = forms.IntegerField()
    periodicidade = forms.CharField(max_length=50)
    necessita_alimentacao = forms.BooleanField(required=False)
    horario_especifico = forms.TimeField(required=False)
    quantidade = forms.IntegerField(min_value=1, initial=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicamento'].label_from_instance = lambda obj: f"{obj.nome} — Estoque: {obj.estoque_minimo} — R$ {obj.preco}"

class AgendarRetornoForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.none(), label='Selecionar paciente ou acompanhante')
    sala = forms.ModelChoiceField(queryset=Sala.objects.all(), label='Sala')
    data_hora = forms.DateTimeField(
        label='Data e Hora da Consulta',
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    def __init__(self, *args, **kwargs):
        paciente_base = kwargs.pop('paciente_base', None)  # <- Aqui está o segredo
        super().__init__(*args, **kwargs)

        if paciente_base:
            qs = Paciente.objects.filter(id=paciente_base.id)
            if paciente_base.acompanhante:
                qs |= Paciente.objects.filter(id=paciente_base.acompanhante.id)
            self.fields['paciente'].queryset = qs

        self.fields['sala'].label_from_instance = lambda obj: f"Sala {obj.numero}"