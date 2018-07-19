# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import programacao.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agrupamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('algoritmo', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('descricao', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('medidas', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AvaliacaoAgrupamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.IntegerField(default=None, null=True, blank=True)),
                ('avaliacao', models.FloatField(default=None, null=True, blank=True)),
                ('feedback', models.TextField(default=None, max_length=1000, null=True, blank=True)),
                ('agrupamento', models.ForeignKey(to='programacao.Agrupamento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AvaliacaoEspecialista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordem_codigo', models.IntegerField(default=None, null=True, blank=True)),
                ('realizada', models.BooleanField(default=False)),
                ('nota', models.FloatField(default=None, null=True, blank=True, validators=[programacao.validators.valida_avaliacao])),
                ('feedback', models.TextField(default=None, max_length=1000, null=True, blank=True)),
                ('observacao', models.TextField(default=None, max_length=1000, null=True, blank=True)),
                ('confirmar_nota', models.BooleanField(default=False)),
                ('confirmar_feedback', models.BooleanField(default=False)),
                ('nova_nota', models.FloatField(default=None, null=True, blank=True, validators=[programacao.validators.valida_avaliacao])),
                ('novo_feedback', models.TextField(default=None, max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arquivo', models.CharField(max_length=100)),
                ('referencia', models.BooleanField(default=False)),
                ('linguagem', models.CharField(default=None, max_length=50, null=True, blank=True, choices=[(b'1', b'C'), (b'2', b'C++'), (b'3', b'Python 2.x'), (b'4', b'Python 3.x'), (b'5', b'Java'), (b'6', b'Pascal'), (b'7', b'Outra')])),
                ('publicar', models.BooleanField(default=False)),
                ('medidas_ok', models.BooleanField(default=False)),
                ('medida_corretude_sintatica', models.BooleanField(default=False)),
                ('medida_corretude_funcional', models.FloatField(default=None, null=True, blank=True)),
                ('medida_complexity', models.FloatField(default=None, null=True, blank=True)),
                ('medida_loc', models.FloatField(default=None, null=True, blank=True)),
                ('medida_lloc', models.FloatField(default=None, null=True, blank=True)),
                ('medida_sloc', models.FloatField(default=None, null=True, blank=True)),
                ('medida_blank', models.FloatField(default=None, null=True, blank=True)),
                ('medida_single_comments', models.FloatField(default=None, null=True, blank=True)),
                ('medida_distinct_operators', models.FloatField(default=None, null=True, blank=True)),
                ('medida_distinct_operands', models.FloatField(default=None, null=True, blank=True)),
                ('medida_total_number_operators', models.FloatField(default=None, null=True, blank=True)),
                ('medida_total_number_operands', models.FloatField(default=None, null=True, blank=True)),
                ('medida_vocabulary', models.FloatField(default=None, null=True, blank=True)),
                ('medida_length', models.FloatField(default=None, null=True, blank=True)),
                ('medida_calculated_length', models.FloatField(default=None, null=True, blank=True)),
                ('medida_volume', models.FloatField(default=None, null=True, blank=True)),
                ('medida_difficulty', models.FloatField(default=None, null=True, blank=True)),
                ('medida_effort', models.FloatField(default=None, null=True, blank=True)),
                ('medida_time', models.FloatField(default=None, null=True, blank=True)),
                ('medida_bugs', models.FloatField(default=None, null=True, blank=True)),
                ('medida_mi', models.FloatField(default=None, null=True, blank=True)),
                ('similaridade_jaccard', models.FloatField(default=None, null=True, blank=True)),
                ('similaridade_text', models.FloatField(default=None, null=True, blank=True)),
                ('similaridade_tree', models.FloatField(default=None, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CriterioEspecialista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criterios', models.TextField(default=None, max_length=1000, null=True, verbose_name=b'Crit\xc3\xa9rios adotados na corre\xc3\xa7\xc3\xa3o', blank=True)),
                ('criterios_adicionais', models.TextField(default=None, max_length=1000, null=True, verbose_name=b'Crit\xc3\xa9rios adicionais adotados na corre\xc3\xa7\xc3\xa3o', blank=True)),
                ('criterio_sintaxe', models.BooleanField(default=False, verbose_name=b'Corretude sintatica')),
                ('criterio_funcional', models.BooleanField(default=False, verbose_name=b'Corretude funcional')),
                ('criterio_qtd_variaveis', models.BooleanField(default=False, verbose_name=b'Quantidade de declara\xc3\xa7\xc3\xb5es de vari\xc3\xa1veis')),
                ('criterio_qtd_atribuicoes', models.BooleanField(default=False, verbose_name=b'Quantidade de atribui\xc3\xa7\xc3\xb5es de valores para vari\xc3\xa1veis')),
                ('criterio_qtd_instrucoes', models.BooleanField(default=False, verbose_name=b'Quantidade de instru\xc3\xa7\xc3\xb5es utilizadas')),
                ('criterio_operadores', models.BooleanField(default=False, verbose_name=b'Uso correto de operadores (relacionais, matem\xc3\xa1ticos, outros)')),
                ('criterio_funcoes_io', models.BooleanField(default=False, verbose_name=b'Uso correto de fun\xc3\xa7\xc3\xb5es de entrada e sa\xc3\xadda')),
                ('criterio_tamanho', models.BooleanField(default=False, verbose_name=b'Tamanho do c\xc3\xb3digo')),
                ('criterio_comentarios', models.BooleanField(default=False, verbose_name=b'Presen\xc3\xa7a de coment\xc3\xa1rios')),
                ('criterio_similaridade_ref', models.BooleanField(default=False, verbose_name=b'Similaridade com uma solu\xc3\xa7\xc3\xa3o esperada')),
                ('criterio_estrutura_decisao', models.BooleanField(default=False, verbose_name=b'Aplicabilidade da estrutura de decis\xc3\xa3o utilizada (ex. if vs. switch)')),
                ('criterio_qtd_decisoes', models.BooleanField(default=False, verbose_name=b'Quantidade de decis\xc3\xb5es utilizadas')),
                ('criterio_profundidade_decisao', models.BooleanField(default=False, verbose_name=b'Profundidade das decis\xc3\xb5es utilizadas')),
                ('criterio_decisoes_compostas', models.BooleanField(default=False, verbose_name=b'Presen\xc3\xa7a/aus\xc3\xaancia de decis\xc3\xb5es compostas')),
                ('criterio_decisoes_aninhadas', models.BooleanField(default=False, verbose_name=b'Presen\xc3\xa7a/aus\xc3\xaancia de decis\xc3\xb5es em sequ\xc3\xaancia')),
                ('criterio_qtd_condicoes', models.BooleanField(default=False, verbose_name=b'Quantidade de condi\xc3\xa7\xc3\xb5es especificadas em cada decis\xc3\xa3o')),
                ('criterio_operadores_logicos', models.BooleanField(default=False, verbose_name=b'Aplicabilidade dos operadores l\xc3\xb3gicos utilizados')),
                ('criterio_qtd_operadores_logicos', models.BooleanField(default=False, verbose_name=b'Quantidade de operadores l\xc3\xb3gicos utilizados')),
                ('criterio_estrutura_repeticao', models.BooleanField(default=False, verbose_name=b'Aplicabilidade da estrutura de repeti\xc3\xa7\xc3\xa3o utilizada (ex. for vs. while)')),
                ('criterio_qtd_est_repeticao', models.BooleanField(default=False, verbose_name=b'Quantidade de estrutura de repeti\xc3\xa7\xc3\xa3o utilizadas')),
                ('criterio_profundidade_repeticao', models.BooleanField(default=False, verbose_name=b'Profundidade das repeti\xc3\xa7\xc3\xb5es')),
                ('criterio_repeticoes_aninhadas', models.BooleanField(default=False, verbose_name=b'Presen\xc3\xa7a/aus\xc3\xaancia de repeti\xc3\xa7\xc3\xb5es aninhadas')),
                ('criterio_eficiencia_tempo', models.BooleanField(default=False, verbose_name=b'Efici\xc3\xaancia em rela\xc3\xa7\xc3\xa3o ao tempo de processamento')),
                ('criterio_eficiencia_memoria', models.BooleanField(default=False, verbose_name=b'Efici\xc3\xaancia em rela\xc3\xa7\xc3\xa3o ao uso de mem\xc3\xb3ria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('experiencia_professor', models.BooleanField(default=False, verbose_name=b'Possui experi\xc3\xaancia como professor')),
                ('nivel_formacao', models.CharField(default=None, choices=[(b'1', b'Doutorado'), (b'2', b'Mestrado'), (b'3', b'Especializa\xc3\xa7\xc3\xa3o'), (b'4', b'Gradua\xc3\xa7\xc3\xa3o')], max_length=50, blank=True, null=True, verbose_name=b'N\xc3\xadvel de forma\xc3\xa7\xc3\xa3o')),
                ('experiencia_monitor', models.BooleanField(default=False, verbose_name=b'Possui experi\xc3\xaancia como monitor de disciplina')),
                ('experiencia_monitor_programacao', models.BooleanField(default=False, verbose_name=b'Possui experi\xc3\xaancia como monitor de disciplina de programa\xc3\xa7\xc3\xa3o')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_especialista', 'view_especialista'), ('view_autor', 'view_autor')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('id_huxley', models.IntegerField(default=None, null=True, blank=True)),
                ('enunciado', models.TextField(default=None, max_length=2000, null=True, blank=True)),
                ('tipo', models.CharField(default=None, max_length=50, null=True, blank=True, choices=[(b'Basico', b'Basico'), (b'Decisao', b'Decis\xc3\xa3o'), (b'Repeticao', b'Repeti\xc3\xa7\xc3\xa3o')])),
                ('entrada', models.TextField(default=None, max_length=2000, null=True, blank=True)),
                ('saida', models.TextField(default=None, max_length=2000, null=True, blank=True)),
                ('conteudo', models.TextField(default=None, max_length=1000, null=True, blank=True)),
                ('publicar', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Similaridade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('algoritmo', models.CharField(default=None, max_length=50, null=True, blank=True, choices=[(b'1', b'Jaccard'), (b'2', b'TextEdit'), (b'3', b'Tree')])),
                ('coeficiente_similaridade', models.FloatField(default=None, null=True, blank=True)),
                ('codigo_referencia', models.ForeignKey(related_name='codigo_referencia', default=None, to='programacao.Codigo')),
                ('codigo_solucao', models.ForeignKey(related_name='codigo_solucao', default=None, to='programacao.Codigo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='criterioespecialista',
            name='especialista',
            field=models.ForeignKey(to='programacao.Especialista'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='criterioespecialista',
            name='problema',
            field=models.ForeignKey(to='programacao.Problema'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codigo',
            name='problema',
            field=models.ForeignKey(default=None, to='programacao.Problema'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='codigo',
            field=models.ForeignKey(to='programacao.Codigo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='especialista',
            field=models.ForeignKey(to='programacao.Especialista'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaliacaoagrupamento',
            name='codigo',
            field=models.ForeignKey(to='programacao.Codigo'),
            preserve_default=True,
        ),
    ]
