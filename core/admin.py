from django.contrib import admin
from .models import (
    Paciente, Enfermeira, Acolhimento, Vacina, Medico, Sala, Consulta,
    Alergia, Medicamento, Prescricao, Equipamento, Ultrassom
)

admin.site.register(Paciente)
admin.site.register(Enfermeira)
admin.site.register(Acolhimento)
admin.site.register(Vacina)
admin.site.register(Medico)
admin.site.register(Sala)
admin.site.register(Consulta)
admin.site.register(Alergia)
admin.site.register(Medicamento)
admin.site.register(Prescricao)
admin.site.register(Equipamento)
admin.site.register(Ultrassom)
