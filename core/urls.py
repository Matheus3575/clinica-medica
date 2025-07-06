from django.urls import path
from core import views

urlpatterns = [
    path('dashboard/', views.medico_dashboard, name='dashboard'),
    path('consultas/agendar/', views.agendar_consulta, name='agendar_consulta'),
    path('consultas/cancelar/', views.cancelar_consulta, name='cancelar_consulta'),
    path('consultas/realizar/', views.realizar_consulta, name='realizar_consulta'),
    path('paciente-info/<int:paciente_id>/', views.paciente_info, name='paciente_info'),
    path('sala-info/<int:sala_id>/', views.sala_info, name='sala_info'),
]