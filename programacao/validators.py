# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError

#Validar a nota se está dentro dos valores permitidos
def valida_avaliacao(value):
    value=float(value)
    if value> 10.0 or value <0:
        raise ValidationError("A avaliação deve ter valores entre 0 e 10!")

