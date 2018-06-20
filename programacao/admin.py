# -*- coding: utf-8 -*-
#import os

from django.contrib import admin
from django.conf import settings

from programacao.models import Problema, Codigo, Especialista, AvaliacaoEspecialista, Agrupamento, AvaliacaoAgrupamento, Similaridade

admin.site.register(Problema)
admin.site.register(Codigo)
admin.site.register(Especialista)
admin.site.register(AvaliacaoEspecialista)

admin.site.register(Agrupamento)
admin.site.register(AvaliacaoAgrupamento)
admin.site.register(Similaridade)
