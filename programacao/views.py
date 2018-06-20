# -*- coding: utf-8 -*-
import os
import re
import sys
#import utils
import shutil
import random

#from utils import *

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse
from django.db import connection, transaction
from django.db.transaction import commit
from django.shortcuts import render, redirect, get_object_or_404

from programacao.forms import EspecialistaForm, RegistroForm, UserEditForm, AvaliacaoEspecialistaForm, ProblemaForm, CriterioBasicoEspecialistaForm, CriterioDecisaoEspecialistaForm, CriterioRepeticaoEspecialistaForm
from programacao.models import Problema, Codigo, Especialista, AvaliacaoEspecialista, Agrupamento, AvaliacaoAgrupamento, Similaridade, CriterioEspecialista

def index(request, template_name='programacao/index.html'):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            u = form.get_user()
            login(request, u)
            if u.has_perm('programacao.view_especialista'):
                return redirect(reverse(viewname='programacao:especialista_index'))
        else: 
            messages.add_message(request, messages.ERROR, 'Usuário não cadastrado ou sem permissão de acesso!')

    form = AuthenticationForm()

    data = {}
    data['form'] = form
    return render(request, template_name, data)


def registro(request, template_name='programacao/registro.html'):
    if request.method == 'POST':
        especialista_form = EspecialistaForm(request.POST or None)
        user_form = RegistroForm(request.POST or None)
        if especialista_form.is_valid() and user_form.is_valid():
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.is_active = True
                user.save()
 
                especialista = especialista_form.save(commit=False)
                especialista.user = user
                especialista.save()

                permission = Permission.objects.get(name='view_especialista')
                user.user_permissions.add(permission)

                messages.add_message(request, messages.INFO, 'Cadastro realizado com sucesso!')
                return redirect('programacao:index')
        else:
            messages.add_message(request, messages.ERROR, 'Erro ao tentar cadastrar!') 

    especialista_form = EspecialistaForm()
    user_form = RegistroForm()

    data = {}
    data['especialista_form'] = especialista_form
    data['user_form'] = user_form
    return render(request, template_name, data)


def sair(request):
    logout(request)
    return redirect('programacao:index')


@login_required
@permission_required('programacao.view_autor')
def admin_index(request, template_name='programacao/admin_index.html'):
    especialistas        = Especialista.objects.all()
    problemas_publicados = Problema.objects.filter(publicar=True)
    problemas            = Problema.objects.filter(publicar=False)

    ordem = False
    n = AvaliacaoEspecialista.objects.filter(realizada=True).count()
    if n == 0 :
        ordem = True

    data = {}
    data['especialistas']        = especialistas
    data['problemas']            = problemas
    data['problemas_publicados'] = problemas_publicados
    data['ordem']                = ordem
    return render(request, template_name, data)


@login_required
@permission_required('programacao.view_autor')
def admin_importar_problemas(request, template_name='programacao/admin_index.html'):
    problemas_selecionados = [280,295,32,294,39,42,49,2,21,342,36,24]

    for problema_id in problemas_selecionados :
        results = list(query_to_dicts(u"SELECT id, name, description, input_format, output_format FROM huxley.problem WHERE id = %d AND name is not NULL AND name != '' AND description is not NULL AND description != '' AND input_format is not NULL AND input_format != '' AND output_format is not NULL AND output_format != ''" % problema_id))

        for row in results :
            nome = remove_acentos(row['name'])
            id_huxley = row['id']
            enunciado = remove_acentos(row['description'])
            entrada = remove_acentos(row['input_format'])
            saida = remove_acentos(row['output_format'])
            Problema.objects.create(nome=nome, id_huxley=id_huxley, enunciado=enunciado, entrada=entrada, saida=saida)

        problema = Problema.objects.get(id_huxley=problema_id)
        # Codigos
        dirsrc = os.path.join(settings.MEDIA_ROOT, 'codigos')
        dirsrc = os.path.join(dirsrc, str(id_huxley))
        for file in os.listdir(dirsrc):
            Codigo.objects.create(arquivo=file, referencia=False, linguagem="Python 3.x", problema=problema)

    especialistas = Especialista.objects.all()
    codigos       = Codigo.objects.all()
    for especialista in especialistas :
        for codigo in codigos :
            AvaliacaoEspecialista.objects.create(codigo=codigo,especialista=especialista)

    problemas = Problema.objects.all()
    problemas_publicados = Problema.objects.filter(publicar=True)
    problemas_count = Problema.objects.count()

    especialistas        = Especialista.objects.all()


    ordem = False
    n = AvaliacaoEspecialista.objects.filter(realizada=True).count()
    if n == 0 :
        ordem = True

    data = {}
    data['especialistas']        = especialistas
    data['problemas']            = problemas
    data['problemas_publicados'] = problemas_publicados
    data['count_problemas']      = problemas_count
    data['ordem']                = ordem
    return render(request, template_name, data)


@login_required
@permission_required('programacao.view_autor')
def admin_editar_problema(request, pk, template_name='programacao/admin_editar_problema.html'):
    problema = get_object_or_404(Problema, pk=pk)

    form = ProblemaForm(request.POST or None, instance=problema)

    if form.is_valid():
        form.save()
        return redirect('programacao:admin_editar_problema', pk)


    codigos = Codigo.objects.filter(problema_id=problema.id)

    data = {}
    data['form'] = form
    data['problema'] = problema
    data['codigos'] = codigos
    return render(request, template_name, data)


@login_required
@permission_required('programacao.view_autor')
def admin_ordem_problemas(request, template_name='programacao/admin_index.html'):
    especialistas = Especialista.objects.all()

    for especialista in especialistas :
        idsbasico    = [280,295,32,294]
        idsdecisao   = [39,42,49,2]
        idsrepeticao = [21,342,36,24]

        qtd_codigos = 10
        # Basico
        ordem_codigo_id = 0
        for i in range(4) :
            n = random.randint(0, len(idsbasico))
            valor = idsbasico[n-1]
            problema = Problema.objects.get(id_huxley=valor)

            # Codigos
            codigos = Codigo.objects.filter(problema_id=problema.id)
            selected_codes = []
            size = len(codigos)
            while len(selected_codes) < qtd_codigos:
                m = random.randint(0, size-1)
                if not(m in selected_codes) :
                    selected_codes.append(codigos[m])

            for codigo in selected_codes :
               a = AvaliacaoEspecialista.objects.get(codigo=codigo,especialista=especialista)
               codigo.publicar = True
               codigo.save()
               a.ordem_codigo=ordem_codigo_id
               a.save()
               ordem_codigo_id += 1

            idsbasico.pop(n-1)

        # Decisao
            n = random.randint(0, len(idsdecisao))
            valor = idsdecisao[n-1]
            problema = Problema.objects.get(id_huxley=valor)

            # Codigos
            codigos = Codigo.objects.filter(problema_id=problema.id)
            selected_codes = []
            size = len(codigos)
            while len(selected_codes) < qtd_codigos:
                m = random.randint(0, size-1)
                if not(m in selected_codes) :
                    selected_codes.append(codigos[m])

            for codigo in selected_codes :
                a = AvaliacaoEspecialista.objects.get(codigo=codigo,especialista=especialista)
                codigo.publicar = True
                codigo.save()
                a.ordem_codigo=ordem_codigo_id
                a.save()
                ordem_codigo_id += 1

            idsdecisao.pop(n-1)

        # Repeticao
            n = random.randint(0, len(idsrepeticao))
            valor = idsrepeticao[n-1]
            problema = Problema.objects.get(id_huxley=valor)

            # Codigos
            codigos = Codigo.objects.filter(problema_id=problema.id)
            selected_codes = []
            size = len(codigos)
            while len(selected_codes) < qtd_codigos:
                m = random.randint(0, size-1)
                if not(m in selected_codes) :
                    selected_codes.append(codigos[m])

            for codigo in selected_codes :
                a = AvaliacaoEspecialista.objects.get(codigo=codigo,especialista=especialista)
                codigo.publicar = True
                codigo.save()
                a.ordem_codigo=ordem_codigo_id
                a.save()
                ordem_codigo_id += 1

            idsrepeticao.pop(n-1)

    #especialistas = Especialista.objects.all()
    problemas_publicados = Problema.objects.filter(publicar=True)
    problemas = Problema.objects.filter(publicar=False)

    data = {}
    data['especialistas'] = especialistas
    data['problemas'] = problemas
    data['problemas_publicados'] = problemas_publicados
    return render(request, template_name, data)



@login_required
@permission_required('programacao.view_autor')
def admin_problema_publicar_codigos(request, pk, template_name='programacao/admin_editar_problema.html'):
    problema = get_object_or_404(Problema, pk=pk)

    form = ProblemaForm(request.POST or None, instance=problema)

    if form.is_valid():
        form.save()
        return redirect('programacao:admin_editar_problema', pk)


    i = 0
    qtd_codigos = 10
    codigos = Codigo.objects.filter(problema_id=problema.id)
    for codigo in codigos :
    	if (i < qtd_codigos) :
            codigo.publicar = True
        else:
        	codigo.publicar = False
        i = i + 1
        codigo.save()

    data = {}
    data['form'] = form
    data['problema'] = problema
    data['codigos'] = codigos
    return render(request, template_name, data)


# @login_required
# @permission_required('programacao.view_autor')
# def admin_ver_agrupamentos(request, pk, template_name='programacao/admin_agrupamentos.html'):
#     problema = get_object_or_404(Problema, pk=pk)
#     avaliacoes_agrupamento_list = AvaliacaoAgrupamento.objects.filter(codigo__problema=problema).order_by('agrupamento__algoritmo', 'agrupamento__medidas', 'grupo')

#     data = {}
#     data['problema'] = problema
#     data['avaliacoes_agrupamento_list'] = avaliacoes_agrupamento_list
#     return render(request, template_name, data)


# @login_required
# @permission_required('programacao.view_autor')
# def admin_notas(request, pk, template_name='programacao/admin_notas.html'):
#     problema = get_object_or_404(Problema, pk=pk)
    
#     codigo_referencia = Codigo.objects.get(problema=problema, referencia=True)
#     id_especialista = 6

@login_required
@permission_required('programacao.view_especialista')
def especialista_index(request, template_name='programacao/especialista_index.html'):
    user           = request.user
    especialista   = Especialista.objects.get(user_id=user.id)
    problemas_list = Problema.objects.filter(publicar=True)
    codigos_list   = Codigo.objects.filter(problema__publicar=True)

    # contadores
    count_problemas                     = len(problemas_list)
    count_avaliacoes_realizadas         = AvaliacaoEspecialista.objects.filter(especialista=especialista,realizada=True).count()
    count_avaliacoes_totais             = count_problemas * 10
    count_confirmar_notas_realizadas    = AvaliacaoEspecialista.objects.filter(especialista=especialista,confirmar_nota=True).count()
    count_confirmar_notas_totais        = count_avaliacoes_totais
    count_confirmar_feedback_realizadas = AvaliacaoEspecialista.objects.filter(especialista=especialista,confirmar_feedback=True).count() 
    count_confirmar_feedback_totais     = count_avaliacoes_totais

    data = {}
    data['problemas_list'] = problemas_list
    # contadores
    data['count_problemas']                     = count_problemas
    data['count_avaliacoes_realizadas']         = count_avaliacoes_realizadas
    data['count_avaliacoes_totais']             = count_avaliacoes_totais
    data['count_confirmar_notas_realizadas']    = count_confirmar_notas_realizadas
    data['count_confirmar_notas_totais']        = count_confirmar_notas_totais
    data['count_confirmar_feedback_realizadas'] = count_confirmar_feedback_realizadas
    data['count_confirmar_feedback_totais']     = count_confirmar_feedback_totais
    return render(request, template_name, data)


@login_required
@permission_required('programacao.view_especialista')
def especialista_edit(request, template_name='programacao/especialista_edit.html'):
    user = request.user
    especialista = Especialista.objects.get(user_id=user.id)

    user_form = UserEditForm(request.POST or None, instance=user)
    especialista_form = EspecialistaForm(request.POST or None, instance=especialista)

    if especialista_form.is_valid() and user_form.is_valid():
        user_form.save()
        especialista_form.save()
        return redirect('programacao:especialista_edit')
    
    data = {}
    data['user_form'] = user_form
    data['especialista_form'] = especialista_form
    return render(request, template_name, data)


@login_required
@permission_required('programacao.view_especialista')
def especialista_visualizar_problema(request, pk, template_name='programacao/especialista_visualizar_problema.html'):
    problema = get_object_or_404(Problema, pk=pk)

    codigos_problema = Codigo.objects.filter(problema=problema)

    user = request.user
    especialista = Especialista.objects.get(user_id=user.id)

    criterios = None
    try:
        criterios = CriterioEspecialista.objects.get(problema=problema, especialista=especialista)
    except:
        pass

    form = CriterioBasicoEspecialistaForm(request.POST or None, instance=criterios)
    if (problema.tipo == 'Basico') :
        form = CriterioBasicoEspecialistaForm(request.POST or None, instance=criterios)
    elif (problema.tipo == 'Decisao') :
        form = CriterioDecisaoEspecialistaForm(request.POST or None, instance=criterios)
    else :
        form = CriterioRepeticaoEspecialistaForm(request.POST or None, instance=criterios)

    if form.is_valid():
        criterio = form.save(commit=False)
        criterio.problema = problema
        criterio.especialista = especialista
        criterio.save()

    data = {}
    data['form'] = form
    data['problema'] = problema
    return render(request, template_name, data)


@login_required
@permission_required('programacao.view_especialista')
def especialista_listar_avaliacoes(request, pk, template_name='programacao/especialista_listar_avaliacoes.html'):
    problema = get_object_or_404(Problema, pk=pk)

    user = request.user
    especialista = Especialista.objects.get(user_id=user.id)

    avaliacao_realizada_list = AvaliacaoEspecialista.objects.filter(codigo__problema=problema,especialista=especialista,codigo__publicar=True,realizada=True).order_by('ordem_codigo')
    codigos_avaliados = []
    for a in avaliacao_realizada_list :
        c = Codigo.objects.get(id=a.codigo_id)
        codigos_avaliados.append(c)

    avaliacao_pendente_list = AvaliacaoEspecialista.objects.filter(codigo__problema=problema,especialista=especialista,codigo__publicar=True,realizada=False).order_by('ordem_codigo')
    codigos_pendentes = []
    for a in avaliacao_pendente_list :
        c = Codigo.objects.get(id=a.codigo_id)
        if not(c in codigos_avaliados) :
            codigos_pendentes.append(c)

    data = {}
    #data['form'] = form
    data['problema'] = problema
    data['codigos_pendentes'] = codigos_pendentes #[0] if codigos_pendentes else None 
    data['codigos_avaliados'] = avaliacao_realizada_list
    return render(request, template_name, data)

@login_required
@permission_required('programacao.view_especialista')#@permission_required('programacao.is_especialista')
def especialista_avaliar(request, pk, template_name='programacao/especialista_avaliar.html'):
    codigo       = get_object_or_404(Codigo, pk=pk)
    problema     = Problema.objects.get(id=codigo.problema_id)
    user         = request.user
    especialista = Especialista.objects.get(user_id=user.id)

    avaliacao    = AvaliacaoEspecialista.objects.get(codigo=codigo, especialista=especialista)
    form         = AvaliacaoEspecialistaForm(request.POST or None, instance=avaliacao)
    source       = codigo.display_text()
    if request.method=='POST':
        if form.is_valid():
            avaliacao_especialista = form.save(commit=False)
            avaliacao_especialista.codigo = codigo
            avaliacao_especialista.especialista = especialista
            avaliacao_especialista.realizada = True
            avaliacao_especialista.save()
            return redirect('programacao:especialista_listar_avaliacoes', pk=codigo.problema_id)

    data = {}
    data['problema'] = problema
    data['codigo'] = codigo
    data['source'] = source
    data['form'] = form
    return render(request, template_name, data)


@login_required
@permission_required('programacao.view_especialista')
def especialista_editar_avaliacao(request, pk, template_name='programacao/especialista_avaliar.html'):
#    user = request.user
#    especialista = Especialista.objects.get(user_id=user.id)
#    codigo = Codigo.objects.get(id=pk)
#    avaliacao = AvaliacaoEspecialista.objects.get(codigo=codigo, especialista=especialista)
    avaliacao = get_object_or_404(AvaliacaoEspecialista, pk=pk)
    form = AvaliacaoEspecialistaForm(request.POST or None, instance=avaliacao)

    source = avaliacao.codigo.display_text()

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('programacao:especialista_listar_avaliacoes', pk=avaliacao.codigo.problema_id)

    data = {}
    data['avaliacao'] = avaliacao
    data['source'] = source
    data['form'] = form
    return render(request, template_name, data)
