# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import DateTimeInput

from programacao.models import Problema, Codigo, Especialista, AvaliacaoEspecialista, Agrupamento, AvaliacaoAgrupamento, Similaridade, CriterioEspecialista


class RegistroForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(), label="Login")
    email = forms.EmailField(widget=forms.TextInput(), label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmação de senha")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super(RegistroForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Senhas não são iguais. Insira os dados novamente.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserEditForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(), label="Login")
    email = forms.EmailField(widget=forms.TextInput(), label="Email")

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class EspecialistaForm(ModelForm):
    class Meta:
        model = Especialista
        fields = ['nome', 'experiencia_professor', 'nivel_formacao', 'experiencia_monitor', 'experiencia_monitor_programacao']


class AvaliacaoEspecialistaForm(ModelForm):
    class Meta:
        model = AvaliacaoEspecialista
        fields = ['nota', 'feedback', 'observacao']
        widgets = {
            'nota': forms.NumberInput(attrs={'step': "0.5"}),
            'feedback': forms.Textarea(attrs={'rows':5, 'cols':200}),
            'observacao': forms.Textarea(attrs={'rows':5, 'cols':200}),
        }

'''
class NovaAvaliacaoEspecialistaForm(ModelForm):
    class Meta:
        model = AvaliacaoEspecialista
        fields = ['nota', 'feedback', 'observacao']
        widgets = {
            'nota': forms.NumberInput(attrs={'step': "0.5"}),
            'feedback': forms.Textarea(attrs={'rows':5, 'cols':200}),
            'observacao': forms.Textarea(attrs={'rows':5, 'cols':200}),
        }
'''

class ProblemaForm(ModelForm):
    class Meta:
        model = Problema
        fields = ['nome', 'id_huxley', 'tipo', 'enunciado', 'entrada', 'saida', 'conteudo', 'publicar']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows':5, 'cols':200}),
        }


class CriterioBasicoEspecialistaForm(ModelForm):
    class Meta:
        model = CriterioEspecialista
        fields = ['criterios','criterio_sintaxe','criterio_funcional','criterio_qtd_variaveis','criterio_qtd_atribuicoes','criterio_qtd_instrucoes','criterio_operadores','criterio_funcoes_io','criterio_tamanho','criterio_comentarios','criterio_similaridade_ref','criterios_adicionais']
        widgets = {
            'criterios': forms.Textarea(attrs={'rows':2, 'cols':200}),
            'criterios_adicionais': forms.Textarea(attrs={'rows':5, 'cols':200}),
        }
        help_texts = {
            'criterios': 'Selecione os critérios que serão utilizados na avaliação de códigos. Utilize este campo caso deseje fornecer alguma observação adicional.',
            'criterios_adicionais': 'Descreva, caso existam, quais seriam os critérios adicionais adotados para avaliar as submissões fornecidas para este problema.',
        }


class CriterioDecisaoEspecialistaForm(ModelForm):
    class Meta:
        model = CriterioEspecialista
        fields = ['criterios','criterio_sintaxe','criterio_funcional','criterio_qtd_variaveis','criterio_qtd_atribuicoes','criterio_qtd_instrucoes','criterio_operadores','criterio_funcoes_io','criterio_tamanho','criterio_comentarios','criterio_similaridade_ref','criterio_estrutura_decisao','criterio_qtd_decisoes','criterio_profundidade_decisao','criterio_decisoes_aninhadas','criterio_decisoes_compostas','criterio_decisoes_aninhadas','criterio_qtd_condicoes','criterio_operadores_logicos','criterio_qtd_operadores_logicos', 'criterios_adicionais']
        widgets = {
            'criterios': forms.Textarea(attrs={'rows':2, 'cols':200}),
            'criterios_adicionais': forms.Textarea(attrs={'rows':5, 'cols':200}),
        }
        help_texts = {
            'criterios': 'Selecione os critérios que serão utilizados na avaliação de códigos. Utilize este campo caso deseje fornecer alguma observação adicional.',
            'criterios_adicionais': 'Descreva, caso existam, quais seriam os critérios adicionais adotados para avaliar as submissões fornecidas para este problema.',
        }


class CriterioRepeticaoEspecialistaForm(ModelForm):
    class Meta:
        model = CriterioEspecialista
        fields = ['criterios','criterio_sintaxe','criterio_funcional','criterio_qtd_variaveis','criterio_qtd_atribuicoes','criterio_qtd_instrucoes','criterio_operadores','criterio_funcoes_io','criterio_tamanho','criterio_comentarios','criterio_similaridade_ref','criterio_estrutura_decisao','criterio_qtd_decisoes','criterio_profundidade_decisao','criterio_decisoes_aninhadas','criterio_decisoes_compostas','criterio_decisoes_aninhadas','criterio_qtd_condicoes','criterio_operadores_logicos','criterio_qtd_operadores_logicos','criterio_estrutura_repeticao','criterio_qtd_est_repeticao','criterio_profundidade_repeticao','criterio_repeticoes_aninhadas','criterio_eficiencia_tempo','criterio_eficiencia_memoria', 'criterios_adicionais']
        widgets = {
            'criterios': forms.Textarea(attrs={'rows':2, 'cols':200}),
            'criterios_adicionais': forms.Textarea(attrs={'rows':5, 'cols':200}),
        }
        help_texts = {
            'criterios': 'Selecione os critérios que serão utilizados na avaliação de códigos. Utilize este campo caso deseje fornecer alguma observação adicional.',
            'criterios_adicionais': 'Descreva, caso existam, quais seriam os critérios adicionais adotados para avaliar as submissões fornecidas para este problema.',
        }
