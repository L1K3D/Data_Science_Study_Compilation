#===IMPORTAÇÃO DAS BIBLIOTECAS===#
from contextlib import nullcontext
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook
import os

#===DECLARAÇÃO DAS VARIAVEIS QUE SÃO LIKADOS OS CAMINHOS DAS PASTAS===#
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


#===IDENTIFICAÇÃO NA PASTA 2===#
for f2 in files2:
    df_2 = pd.read_excel(caminho2 + "/" + f2)

#===CRIAÇÃO DO ARQUIVO EXCEL CONSOLIDADO===#
df_final = pd.DataFrame()
type(df_final)

df_final = pd.concat([df_1, df_2])

print(df_final)
print(f1)
print(f2)

#===SISTEMA DE SALVAMENTO DA PASTA GERADA===#
df_final.to_excel(r'Insira o caminho onde o novo arquivo será salvo \Nome do arquivo.xlsx')
