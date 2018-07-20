#-*- coding: latin1 -*-
import os
#import re
#import sys
#import shutil
#import random
#import MySQLdb
#import unicodedata

import django
# django project name is adleads, replace adleads with your project name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "safiraweb.settings")
django.setup()

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

problemas = Problema.objects.all()
# iterando problemas
for problema in problemas:
    print("============================")
    print(problema.nome)
    print(problema.id_huxley)
    print("============================")

    codigos = Codigo.objects.filter(problema=problema,publicar=False)[:10]
    # iterando codigos
    for code in codigos:
        code.publicar_confirmar = True
        code.save()
