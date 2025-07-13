from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from core.models import Medico, Paciente, Acolhimento, Consulta, Sala, Equipamento, Ultrassom, Alergia, Prescricao,Medicamento
from core.forms import AgendarConsultaForm
from .forms import FinalizarConsultaForm,PrescricaoForm, AgendarRetornoForm, MedicoUpdateForm
from django.contrib import messages
from django.utils import timezone
from datetime import datetime , time, timedelta, date
from django.contrib.auth import logout
from django.utils.dateparse import parse_date
from .utils import parse_dosagem, extrair_numero_antes_primeira_unidade
from django.utils.timezone import now, make_aware
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone


@login_required
def medico_dashboard(request):
    medico = Medico.objects.filter(user=request.user).first()
    if not medico:
        return redirect('logout')  # segurança

    context = {'medico': medico}
    return render(request, 'medico_dashboard.html', context)

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

    return render(request, 'agendar_consulta.html', {'form': form, 'alerta': alerta, 'sucesso': sucesso})

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
def consultas_dia(request):
    data = request.GET.get('data')
    if not data:
        return JsonResponse({'erro': 'Data não fornecida'}, status=400)

    try:
        data_obj = parse_date(data)
        if not data_obj:
            raise ValueError("Formato de data inválido")

        inicio = datetime.combine(data_obj, time.min)
        fim = datetime.combine(data_obj, time.max)

        consultas = Consulta.objects.filter(data_hora__range=(inicio, fim)).select_related('paciente', 'sala')

        resultado = [
            {
                'nome': consulta.paciente.nome,
                'hora': consulta.data_hora.strftime('%H:%M'),
                'sala': consulta.sala.numero
            } for consulta in consultas
        ]

        return JsonResponse({'consultas': resultado})

    except ValueError as e:
        return JsonResponse({'erro': str(e)}, status=400)


@login_required
def cancelar_consulta(request):
    medico = Medico.objects.filter(user=request.user).first()
    if not medico:
        return redirect('logout')  # segurança

    mensagem = None

    if request.method == 'POST':
        consulta_id = request.POST.get('consulta_id')
        try:
            # Inclui apenas consultas de hoje ou futuras
            hoje_inicio = make_aware(datetime.combine(date.today(), time.min))
            consulta = Consulta.objects.get(id=consulta_id, medico=medico, data_hora__gte=hoje_inicio)
            consulta.delete()
            mensagem = "Consulta cancelada com sucesso!"
        except Consulta.DoesNotExist:
            mensagem = "Consulta não encontrada, já ocorreu ou você não tem permissão para cancelar."

    # Consultas a partir de hoje, inclusive
    hoje_inicio = make_aware(datetime.combine(date.today(), time.min))
    consultas = Consulta.objects.filter(
        medico=medico,
        data_hora__gte=hoje_inicio
    ).order_by('data_hora')

    context = {
        'consultas': consultas,
        'mensagem': mensagem,
    }
    return render(request, 'cancelar_consulta.html', context)


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
    consulta = consultas.filter(id=consulta_id).first() if consulta_id else consultas.first()
    if not consulta:
        consulta = consultas.first()

    paciente = consulta.paciente
    acolhimento = Acolhimento.objects.filter(paciente=paciente).order_by('-data_hora').first()

    idade = (date.today() - paciente.data_nascimento).days // 365
    imc = None
    if acolhimento and acolhimento.peso and acolhimento.altura:
        imc = acolhimento.peso / (acolhimento.altura ** 2)

    alergias = Alergia.objects.filter(paciente=paciente)
    consultas_passadas = Consulta.objects.filter(
        paciente=paciente,
        data_hora__lte=timezone.now()
    ).order_by('-data_hora')

    form = FinalizarConsultaForm()
    prescricao_form = PrescricaoForm()
    agendar_form = AgendarRetornoForm(paciente_base=paciente)

    # Preparar lista com idade e IMC para todas as consultas do dia
    lista_consultas = []
    for c in consultas:
        p = c.paciente
        p_idade = (date.today() - p.data_nascimento).days // 365
        acol = Acolhimento.objects.filter(paciente=p).order_by('-data_hora').first()
        p_imc = None
        if acol and acol.peso and acol.altura:
            p_imc = acol.peso / (acol.altura ** 2)
        lista_consultas.append({
            'consulta': c,
            'idade': p_idade,
            'imc': p_imc,
        })

    if request.method == 'POST':
        if 'finalizar' in request.POST:
            form = FinalizarConsultaForm(request.POST)
            if form.is_valid():
                consulta.consulta_descritiva = form.cleaned_data['consulta_descritiva']
                consulta.save()
                messages.success(request, "Consulta finalizada com sucesso.")
                return redirect(f"{request.path}?id={consulta.id}")

        elif 'adicionar_prescricao' in request.POST:
            prescricao_form = PrescricaoForm(request.POST)
            if prescricao_form.is_valid():
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
                    prescricao_form = PrescricaoForm()

        elif 'agendar_nova' in request.POST:
            agendar_form = AgendarRetornoForm(request.POST, paciente_base=paciente)
            if agendar_form.is_valid():
                paciente_novo = agendar_form.cleaned_data['paciente']
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

    prescricoes = Prescricao.objects.filter(consulta=consulta)

    return render(request, 'realizar_consulta.html', {
        'lista_consultas': lista_consultas,
        'consulta': consulta,
        'form': form,
        'alergias': alergias,
        'consultas_passadas': consultas_passadas,
        'prescricao_form': prescricao_form,
        'prescricoes': prescricoes,
        'agendar_form': agendar_form,
        'idade': idade,
        'imc': imc,
    })


@login_required
def buscar_medicamentos(request):
    termo = request.GET.get('q', '').lower()
    medicamentos = Medicamento.objects.filter(nome__icontains=termo).order_by('nome')[:10]
    resultados = [{'id': m.id, 'nome': m.nome} for m in medicamentos]
    return JsonResponse(resultados, safe=False)

@login_required
def medico_perfil(request):
    medico = get_object_or_404(Medico, user=request.user)
    if request.method == 'POST':
        form = MedicoUpdateForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return render(request, 'medico_perfil.html', {'form': form, 'success': True})
        else:
            form = MedicoUpdateForm(instance=medico)
            return render(request, 'medico_perfil.html', {'form': form})
    else:
        form = MedicoUpdateForm(instance=medico)
        return render(request, 'medico_perfil.html', {'form': form})

@login_required
def paciente_perfil(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    consultas = Consulta.objects.filter(paciente = paciente).order_by('-data_hora')
    alergias = Alergia.objects.filter(paciente=paciente)
    acolhimento = Acolhimento.objects.filter(paciente=paciente).order_by('-data_hora').first()
    prescricoes = Prescricao.objects.filter(consulta__paciente=paciente)
    hoje = date.today()
    idade = hoje.year - paciente.data_nascimento.year - ((hoje.month, hoje.day) < (paciente.data_nascimento.month, paciente.data_nascimento.day))


    return render(request, 'paciente_perfil.html', {
        'paciente': paciente,
        'consultas': consultas,
        'alergias': alergias,
        'acolhimento': acolhimento,
        'prescricoes': prescricoes,
        'idade': idade,
    })
    
def logout_view(request):
    logout(request)
    return redirect('login')