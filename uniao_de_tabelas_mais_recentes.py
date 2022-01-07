#===IMPORTAÇÃO DAS BIBLIOTECAS===#
from contextlib import nullcontext
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook
import os

#===DECLARAÇÃO DAS VARIAVEIS QUE SÃO LINKADOS OS CAMINHOS DAS PASTAS===#
caminho1 = r'Insira o caminho da primeira pasta'
caminho2 = r'Insira o caminho da segunda pasta'

#===DECLARAÇÃO DE OBTENÇÃO DOS ARQUIVOS PRESENTES NAS PASTAS===#
for lista1 in os.listdir(caminho1):
    print(lista1)

for listas2 in os.listdir(caminho2):
    print(listas2)

#===JUNÇÃO DOS ARQUIVOS PRESENTES NAS PASTAS EM UMA LISTA DE GERAÇÃO DENTRO DO PYTHON===#
#===LISTA 1 - ARQUIVOS PRESENTES NA PASTA APRESENTADA EM "caminho1"===# 
files1 = []

for unite1 in os.listdir(caminho1):
    files1.append(unite1)
print(files1)

#===LISTA 2 - ARQUIVOS PRESENTES NA PASTA APRESENTADA EM "caminho2"===#
files2 = []

for unite2 in os.listdir(caminho2):
    files2.append(unite2)
print(files2)

#===CRIAÇÃO DE UMA TERCEIRA LISTA QUE UNE OS CONTEUDOS DAS DUAS LISTAS POSTERIORMENTE APRESENTADAS===#
files3 = files1 + files2
print(files3)

#===PROCESSO DE IDENTIFICAÇÃO DE QUAL FOI ÚLTIMO ARQUIVO EXCEL ADICIONADO NA PASTA===#
#===IDENTIFICAÇÃO NA PASTA 1===#
for f1 in files1:
    df_1 = pd.read_excel(caminho1 + "/" + f1)
print(df_1)
print(df_1.shape)

#===IDENTIFICAÇÃO NA PASTA 2===#
for f2 in files2:
    df_2 = pd.read_excel(caminho2 + "/" + f2)
print(df_2)
print(df_2.shape)
    
#===CRIAÇÃO DO ARQUIVO EXCEL CONSOLIDADO===#
df_final = pd.DataFrame()
type(df_final)
df_final = pd.concat([df_1, df_2])
print(df_final)
print(df_final.shape)

#===SISTEMA DE SALVAMENTO DA PASTA GERADA===#
df_final.to_excel(r'Insira o caminho onde o novo arquivo será salvo \Nome do arquivo.xlsx')







#===NOTAS===#
#1. NÃO delete os 'r' antes dos endereçamentos das pastas de procura e da pasta de salvamento, ou o arquivo reconhecera os endereços como strings e não como indexes;
#2. NÃO use caracteres especiais, acentos, ou espaçoos na hora de nomear os indexes, as pastas ou os arquivos de excel;
#3. NÃO mude o tipo de arquivo que seráa criado, ou o arquivo que você obterá não será um arquivo Excel (.xlxs).
