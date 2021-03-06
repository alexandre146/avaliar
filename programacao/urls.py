# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from programacao import views

urlpatterns = patterns('',
    # Registro e autorização
    url(r'^$', views.index, name='index'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^sair/$', views.sair, name='sair'),
    # Avaliador especialista
    url(r'^especialista/$', views.especialista_index, name='especialista_index'),
    url(r'^especialista/edit/$', views.especialista_edit, name='especialista_edit'),
    url(r'^especialista/visualizar/problema/(?P<pk>\d+)$', views.especialista_visualizar_problema, name='especialista_visualizar_problema'),
    url(r'^especialista/avaliar/(?P<pk>\d+)$', views.especialista_avaliar, name='especialista_avaliar'),
    url(r'^especialista/avaliar/editar/(?P<pk>\d+)$', views.especialista_editar_avaliacao, name='especialista_editar_avaliacao'),
    url(r'^especialista/avaliar/lista/(?P<pk>\d+)$', views.especialista_listar_avaliacoes, name='especialista_listar_avaliacoes'),
    url(r'^especialista/nota/confirmar/lista/(?P<pk>\d+)$', views.especialista_nota_listar_confirmacoes, name='especialista_nota_listar_confirmacoes'),
    url(r'^especialista/nota/confirmar/(?P<pk>\d+)$', views.especialista_nota_confirmar, name='especialista_nota_confirmar'),
    url(r'^especialista/feedback/confirmar/lista/(?P<pk>\d+)$', views.especialista_feedback_listar_confirmacoes, name='especialista_feedback_listar_confirmacoes'),
    url(r'^especialista/feedback/confirmar/(?P<pk>\d+)$', views.especialista_feedback_confirmar, name='especialista_feedback_confirmar'),
    # Admin
    url(r'^admin/$', views.admin_index, name='admin_index'),
    url(r'^admin/ordem/problemas/$', views.admin_ordem_problemas, name='admin_ordem_problemas'),
    url(r'^admin/importar/problemas/$', views.admin_importar_problemas, name='admin_importar_problemas'),
    url(r'^admin/editar/problema/(?P<pk>\d+)$', views.admin_editar_problema, name='admin_editar_problema'),
    url(r'^admin/problema/publicar/codigo/(?P<pk>\d+)$', views.admin_problema_publicar_codigos, name='admin_problema_publicar_codigos'),
)
