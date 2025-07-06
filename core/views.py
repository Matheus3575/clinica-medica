from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import date
from core.models import Medico, Paciente, Acolhimento, Consulta, Sala, Equipamento, Ultrassom, Alergia, Prescricao,Medicamento
from core.forms import AgendarConsultaForm
from datetime import timedelta
from .forms import FinalizarConsultaForm,PrescricaoForm, AgendarRetornoForm
from django.contrib import messages
from django.utils import timezone
from datetime import datetime , time
from django.contrib.auth import logout

@login_required
def medico_dashboard(request):
    medico = Medico.objects.filter(user=request.user).first()
    if not medico:
        return redirect('logout')  # segurança

    context = {'medico': medico}
    return render(request, 'core/medico_dashboard.html', context)

@login_required
def agendar_consulta(request):
    alerta = None
    sucesso = None

    # Pegue o médico logado (você precisa disso para a consulta)
    medico = Medico.objects.filter(user=request.user).first()
    if not medico:
        return redirect('logout')  # segurança, caso não encontre médico

    if request.method == 'POST':
        form = AgendarConsultaForm(request.POST)
        if form.is_valid():
            paciente = form.cleaned_data['paciente']

            acolhimento = Acolhimento.objects.filter(paciente=paciente).order_by('-data_hora').first()
            idade = (date.today() - paciente.data_nascimento).days // 365

            imc = None
            if acolhimento and acolhimento.peso and acolhimento.altura:
                imc = acolhimento.peso / (acolhimento.altura ** 2)

            if idade > 65 and imc and imc > 25:
                alerta = f"ATENÇÃO: Paciente {paciente.nome} tem {idade} anos e IMC {imc:.1f} (sobrepeso)."

            Consulta.objects.create(
                paciente=paciente,
                medico=medico,
                sala=form.cleaned_data['sala'],
                data_hora=form.cleaned_data['data_hora'],
                CID11='',
                valor=None,
                forma_pagamento=None,
                consulta_descritiva=''
            )
            sucesso = "Consulta agendada com sucesso!"
            form = AgendarConsultaForm()  # limpa o form após salvar
    else:
        form = AgendarConsultaForm()

    return render(request, 'core/agendar_consulta.html', {'form': form, 'alerta': alerta, 'sucesso': sucesso})

@login_required
def paciente_info(request, paciente_id):
    try:
        paciente = Paciente.objects.get(id=paciente_id)
        acolhimento = Acolhimento.objects.filter(paciente=paciente).order_by('-data_hora').first()
        idade = (date.today() - paciente.data_nascimento).days // 365
        imc = None
        if acolhimento and acolhimento.peso and acolhimento.altura:
            imc = round(acolhimento.peso / (acolhimento.altura ** 2), 1)
        return JsonResponse({'nome': paciente.nome, 'idade': idade, 'imc': imc})
    except Paciente.DoesNotExist:
        return JsonResponse({'erro': 'Paciente não encontrado'}, status=404)

@login_required
def sala_info(request, sala_id):
    try:
        sala = Sala.objects.get(id=sala_id)
        equipamentos = Equipamento.objects.filter(sala=sala)
        hoje = date.today()

        equipamentos_data = []
        for eq in equipamentos:
            equipamentos_data.append({
                'nome': eq.nome,
                'vencido': eq.data_manutencao and (hoje - eq.data_manutencao).days > (5 * 365),
            })

        try:
            us = sala.ultrassom
            ultrassom_info = {
                'modelo': us.modelo,
                'fabricante': us.fabricante,
            }
        except Ultrassom.DoesNotExist:
            ultrassom_info = None

        return JsonResponse({
            'numero_sala': sala.numero,
            'equipamentos': equipamentos_data,
            'ultrassom': ultrassom_info,
        })

    except Sala.DoesNotExist:
        return JsonResponse({'erro': 'Sala não encontrada'}, status=404)


@login_required
def cancelar_consulta(request):
    medico = Medico.objects.filter(user=request.user).first()
    if not medico:
        return redirect('logout')  # segurança

    mensagem = None

    if request.method == 'POST':
        consulta_id = request.POST.get('consulta_id')
        try:
            consulta = Consulta.objects.get(id=consulta_id, medico=medico)
            consulta.delete()
            mensagem = "Consulta cancelada com sucesso!"
        except Consulta.DoesNotExist:
            mensagem = "Consulta não encontrada ou você não tem permissão para cancelar."

    consultas = Consulta.objects.filter(medico=medico).order_by('data_hora')

    context = {
        'consultas': consultas,
        'mensagem': mensagem,
    }
    return render(request, 'core/cancelar_consulta.html', context)

@login_required
def realizar_consulta(request):
    medico = Medico.objects.filter(user=request.user).first() 
    agora = timezone.now()
    hoje_inicio = datetime.combine(agora.date(), time.min).replace(tzinfo=timezone.get_current_timezone())

    consultas = Consulta.objects.filter(
        data_hora__gte=hoje_inicio,
        data_hora__lte=agora
    ).order_by('data_hora')

    if not consultas.exists():
        messages.error(request, "Nenhuma consulta disponível para realização hoje.")
        return redirect('dashboard')

    consulta_id = request.GET.get('id')
    if consulta_id:
        consulta = consultas.filter(id=consulta_id).first()
        if not consulta:
            consulta = consultas.first()
    else:
        consulta = consultas.first()

    alergias = Alergia.objects.filter(paciente=consulta.paciente)
    consultas_passadas = Consulta.objects.filter(
    	paciente=consulta.paciente,
    	data_hora__lte=timezone.now()  # todas até agora
    ).order_by('-data_hora')

    form = FinalizarConsultaForm(request.POST or None)
    prescricao_form = PrescricaoForm(request.POST or None)
    prescricoes = Prescricao.objects.filter(consulta=consulta)
    agendar_form = AgendarRetornoForm(request.POST or None, paciente_base=consulta.paciente)

    if request.method == 'POST':
    	# Finalizar consulta
    	if 'consulta_descritiva' in request.POST and form.is_valid():
        	consulta.consulta_descritiva = form.cleaned_data['consulta_descritiva']
        	consulta.save()
        	messages.success(request, "Consulta finalizada com sucesso.")
        	return redirect(f"{request.path}?id={consulta.id}")

    	# Criar prescrição
    	if 'medicamento' in request.POST and prescricao_form.is_valid():
        	medicamento = prescricao_form.cleaned_data['medicamento']
        	quantidade = prescricao_form.cleaned_data['quantidade']

        	if medicamento.estoque_minimo < quantidade:
            		messages.error(request, f"Estoque insuficiente de {medicamento.nome}. Disponível: {medicamento.estoque_minimo}")
        	else:
            		Prescricao.objects.create(
                		consulta=consulta,
                		medicamento=medicamento,
                		dosagem=prescricao_form.cleaned_data['dosagem'],
                		duracao=prescricao_form.cleaned_data['duracao'],
                		periodicidade=prescricao_form.cleaned_data['periodicidade'],
                		necessita_alimentacao=prescricao_form.cleaned_data['necessita_alimentacao'],
                		horario_especifico=prescricao_form.cleaned_data['horario_especifico'],
                		quantidade=quantidade
            	)
            		medicamento.estoque_minimo -= quantidade
            		medicamento.save()
            		messages.success(request, f"Prescrição adicionada. Estoque de {medicamento.nome} atualizado.")
            		return redirect(f"{request.path}?id={consulta.id}")

    	elif 'agendar_nova' in request.POST:
            if agendar_form.is_valid():
                paciente_novo = agendar_form.cleaned_data['paciente']

                # Cria a nova consulta direto, sem alerta de IMC ou idade
                Consulta.objects.create(
                    paciente=paciente_novo,
                    medico=medico,
                    sala=agendar_form.cleaned_data['sala'],
                    data_hora=agendar_form.cleaned_data['data_hora'],
                    CID11='',
                    valor=None,
                    forma_pagamento=None,
                    consulta_descritiva=''
                )
                messages.success(request, "Nova consulta agendada com sucesso!")
                return redirect(f"{request.path}?id={consulta.id}")

    return render(request, 'core/realizar_consulta.html', {
        'consultas': consultas,
        'consulta': consulta,
        'form': form,
        'alergias': alergias,
        'consultas_passadas': consultas_passadas,
        'prescricao_form': prescricao_form,
        'prescricoes': prescricoes,
	'agendar_form': agendar_form,
    })
    
    def logout_view(request):
    	logout(request)
    	return redirect('login')