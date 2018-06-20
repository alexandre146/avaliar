#-*- coding: utf-8 -*-

import os
import re
import sys
import shutil
import MySQLdb
import unicodedata

#from itertools import *
#from pexpect import spawn
from django.db import connection
from unicodedata import normalize
from django.conf import settings

def query_to_dicts(query_string, *query_args):
    db = MySQLdb.connect(host = '127.0.0.1', user = 'root', passwd = 'root', db = 'huxley', port = 3306)
    cursor = db.cursor()
    cursor.execute(query_string, query_args)
    col_names = [desc[0] for desc in cursor.description]
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        row_dict = dict(izip(col_names, row))
        yield row_dict
    return


def remove_acentos(text, enc='utf-8'):
    saida = ''
    try :
        saida = normalize('NFKD', text.decode('latin1', errors='ignore')).encode('ASCII','ignore')
    except:
        saida = normalize('NFKD', text.decode(enc, errors='ignore')).encode('ASCII','ignore')
    return saida


def remove_comments(text, language):
    '''
    remove comentarios de codigos C e Python
    http://www.pyregex.com/
    '''

    pattern = ''
    if language == "C" or language == "c" :
        pattern = r"""
	                    ##  --------- COMMENT ---------
	   /\*              ##  Start of /* ... */ comment
	   [^*]*\*+         ##  Non-* followed by 1-or-more *'s
	   (                ##
	     [^/*][^*]*\*+  ##
	   )*               ##  0-or-more things which don't start with /
	                    ##    but do end with '*'
	   /                ##  End of /* ... */ comment
	 |                  ##  -OR-  various things which aren't comments:
	   (                ## 
	                    ##  ------ " ... " STRING ------
	     "              ##  Start of " ... " string
	     (              ##
	       \\.          ##  Escaped char
	     |              ##  -OR-
	       [^"\\]       ##  Non "\ characters
	     )*             ##
	     "              ##  End of " ... " string
	   |                ##  -OR-
                        ##
	                    ##  ------ ' ... ' STRING ------
         '              ##  Start of ' ... ' string
	     (              ##
	       \\.          ##  Escaped char
	     |              ##  -OR-
	       [^'\\]       ##  Non '\ characters
	     )*             ##
	     '              ##  End of ' ... ' string
	   |                ##  -OR-
	                    ##
	                    ##  ------ ANYTHING ELSE -------
	     .              ##  Anything other char
	     [^/"'\\]*      ##  Chars which doesn't start a comment, string
	   )                ##    or escape
        """
    else :
        pattern = r"""
          (?P<comments>
              \s*\#(?![-]\*[-])(?:[^\r\n])* # single line comments
              | '''(?:                 # Tripple-quoted can contain...
                  [^']               | # a non-quote
                  \\'                | # a backslashed quote
                  '{1,2}(?!')          # one or two quotes
                               )*'''
          )
        | (?P<code>
                "{3}(?:\\.|[^\\])*"{3}          # triple double quotes
              | '{3}(?:\\.|[^\\])*'{3}          # triple single quotes
              | "(?:\\.|[^"\\])*"               # double quotes
              | '(?:\\.|[^'])*'                 # single quotes
              | .[^\#"']*                       # everything else
          )
    	"""
#  |\s*\#(?:[^\r\n])*    # single line comments
#  \#\s*[-]\*[-][Cc]oding:\s*.*[-]\*[-]$   # coding declaration
    regex = re.compile(pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
    noncomments = [m.group(2) for m in regex.finditer(text) if m.group(2)]

    return "".join(noncomments)

def remove_comments_main(arquivo, linguagem='C'):
    '''
    remove comentarios de codigos C e Python
    '''
    filename = arquivo
    language = linguagem
    code_w_comments = open(filename).read()
    code_wo_comments = remove_comments(code_w_comments, language)
    fh = open(filename+".nocomments", "w")
    fh.write(code_wo_comments)
    fh.close()


def select_language(linguagem='C'):
    linguagem = linguagem.upper()
    if (linguagem == 'C') :
        return "C"
    elif (linguagem == 'CPP') :
        return "C++"
    elif (linguagem == 'PYTHON') :
        return "Python 2.x"
    elif (linguagem == 'PYTHON3.2') :
        return "Python 3.x"
    elif (linguagem == 'JAVA') :
        return "Java"
    elif (linguagem == 'PASCAL') :
        return "Pascal"
    else :
        return "outra"


def select_extensao(linguagem='C'):
    linguagem = linguagem.upper()
    if (linguagem == 'C') :
        return ".c"
    elif (linguagem == 'C++') :
        return ".cpp"
    elif (linguagem == 'PYTHON 2.X') or (linguagem == 'PYTHON 3.X'):
        return ".py"
    elif (linguagem == 'JAVA') :
        return ".java"
    elif (linguagem == 'PASCAL') :
        return ".pas"
    else :
        return ".outra"


def corretude(codigo):
    if (codigo == 0) :
        # 0 = CORRECT -> Submissão correta
        return (100, True)
    elif (codigo == 1) or (codigo == 9):
        #1 = WRONG_ANSWER -> Submissão gerou resposta errada 
        #9 = PRESENTATION_ERROR -> Submissão correta, porém a resposta não está no formato esperado
        return (0, True)
    elif (codigo == 2) or (codigo == 4):
        #2 = RUNTIME_ERROR -> Submissão causou um erro de execução
        #4 = EMPTY_ANSWER  -> Submissão não gerou respostas para a entrada dada
        return (0, False)
    elif (codigo == 3) :
        #3 = COMPILATION_ERROR -> Submissão causou um erro de compilação
        return (0, False)
    else :
        #5 = TIME_LIMIT_EXCEEDED ->  Submissão superou o limite de tempo de avaliação
        #6 = WAITING -> Aguardando avaliação
        #7 = EMPTY_TEST_CASE -> Submissão para problema sem casos de teste
        #8 = WRONG_FILE_NAME -> Nome do arquivo de submissão inválido
        #10 = HUXLEY_ERROR -> O sistema apresentou um erro ao tentar avaliar
        return (0, False)

def testar_solucao(codigo, entradas, saida):
    interpretador = 'python '
    if ( (codigo.linguagem).upper() == 'PYTHON 3.X')  :
        interpretador = 'python3 '
#    else : #( (codigo.linguagem).upper() == 'PYTHON 2.X')  :
#        interpretador = 'python2 '

    submissao = os.path.join(settings.MEDIA_ROOT, 'codigos', str(codigo.problema.id_huxley), str(codigo.id_turma), str(codigo.arquivo))
    if (os.path.exists(submissao)):
        child = spawn(interpretador + submissao)
        for i in entradas :
            child.sendline(str(i))
        if (child.readlines()[-1].strip().upper() == saida.strip().upper()) :
            return True
        else: 
            return False

