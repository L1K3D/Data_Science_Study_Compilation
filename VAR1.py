#===IMPORTAÇÃO DAS BIBLIOTECAS===#
#===LIBRARY IMPORTATION===#
#===IMPORTACIÓN DE BIBLIOTECAS===#
from contextlib import nullcontext
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook
import os

#===DECLARAÇÃO DAS VARIAVEIS QUE SÃO LINKADOS OS CAMINHOS DAS PASTAS===#
#===DECLARATION OF THE VARIABLES THAT ARE LINKED TO THE FOLDER PATHS===#
#===DECLARACIÓN DE LAS VARIABLES VINCULADAS A LAS CARPETAS===#
caminho1 = r'Enter first folder adress'
caminho2 = r'Enter second folder adress'

#===DECLARAÇÃO DE OBTENÇÃO DOS ARQUIVOS PRESENTES NAS PASTAS===#
#===DECLARATION OF OBTAINING THE FILES PRESENT IN THE FOLDERS===#
#===DECLARACIÓN DE OBTENCIÓN DE LOS ARCHIVOS PRESENTES EN LAS CARPETAS===#
for lista1 in os.listdir(caminho1):
    print(lista1)

for listas2 in os.listdir(caminho2):
    print(listas2)

#===JUNÇÃO DOS ARQUIVOS PRESENTES NAS PASTAS EM UMA LISTA DE GERAÇÃO DENTRO DO PYTHON===#
#===JOINING THE FILES IN THE FOLDERS IN A GENERATION LIST WITHIN PYTHON===#
#===UNIR LOS ARCHIVOS DE LAS CARPETAS EN UNA LISTA DE GENERACIÓN DENTRO DE PYTHON===#

#===LISTA 1 - ARQUIVOS PRESENTES NA PASTA APRESENTADA EM "caminho1"===#
#===LIST 1 - FILES IN THE FOLDER PRESENTED IN "caminho1"===#
#===LISTA 1 - ARCHIVOS EN LA CARPETA PRESENTADOS EN "caminho1"===#
files1 = []

for unite1 in os.listdir(caminho1):
    files1.append(unite1)
print(files1)

#===LISTA 2 - ARQUIVOS PRESENTES NA PASTA APRESENTADA EM "caminho2"===#
#===LIST 2 - FILES IN THE FOLDER PRESENTED IN "caminho2"===#
#===LISTA 2 - ARCHIVOS EN LA CARPETA PRESENTADOS EN "caminho2"===#
files2 = []

for unite2 in os.listdir(caminho2):
    files2.append(unite2)
print(files2)

#===CRIAÇÃO DE UMA TERCEIRA LISTA QUE UNE OS CONTEUDOS DAS DUAS LISTAS POSTERIORMENTE APRESENTADAS===#
#===CREATION OF A THIRD LIST THAT JOINS THE CONTENTS OF THE TWO LISTS SUBMITTED===#
#===CREACIÓN DE UNA TERCERA LISTA QUE SE UNE A LOS CONTENIDOS DE LAS DOS LISTAS PRESENTADAS===#
files3 = files1 + files2
print(files3)

#===PROCESSO DE IDENTIFICAÇÃO DE QUAL FOI ÚLTIMO ARQUIVO EXCEL ADICIONADO NA PASTA===#
#===IDENTIFICATION PROCESS OF WHICH EXCEL FILE WAS LAST ADDED TO FOLDER===#
#===PROCESO DE IDENTIFICACIÓN DEL ARCHIVO EXCEL QUE FUE AÑADIDO POR ÚLTIMA VEZ EN LA CARPETA===#

#===IDENTIFICAÇÃO NA PASTA 1===#
#===IDENTIFICATION IN FOLDER 1===#
#===IDENTIFICACIÓN EN CARPETA 1===#
for f1 in files1:
    df_1 = pd.read_excel(caminho1 + "/" + f1)
print(df_1)
print(df_1.shape)

#===IDENTIFICAÇÃO NA PASTA 2===#
#===IDENTIFICATION IN FOLDER 2===#
#===IDENTIFICACIÓN EN CARPETA 2===#
for f2 in files2:
    df_2 = pd.read_excel(caminho2 + "/" + f2)
print(df_2)
print(df_2.shape)
    
#===CRIAÇÃO DO ARQUIVO EXCEL CONSOLIDADO===#
#===CREATING THE EXCEL CONSOLIDATED FILE===#
#===CREANDO EL ARCHIVO CONSOLIDADO DE EXCEL===#
df_final = pd.DataFrame()
type(df_final)
df_final = pd.concat([df_1, df_2])
print(df_final)
print(df_final.shape)

#===SISTEMA DE SALVAMENTO DA PASTA GERADA===#
#===FOLDER GENERATED SAVE SYSTEM===#
#===SISTEMA DE GUARDADO GENERADO POR CARPETAS===#
df_final.to_excel(r'Enter the folder adress where the new Excel file will be saved \File name.xlsx')







#===NOTAS===#
#1. NÃO delete os 'r' antes dos endereçamentos das pastas de procura e da pasta de salvamento, ou o programa reconhecerá os endereços como strings e não como indexes;
#2. NÃO use caracteres especiais, acentos, ou espaçoos na hora de nomear os indexes, as pastas ou os arquivos de excel;
#3. NÃO mude o tipo de arquivo que será criado, ou o arquivo que você obterá não será um arquivo Excel ('.xlsx').

#===NOTES===#
#1. DO NOT delete the 'r' before the search folder and save folder addresses, or the program will recognize the addresses as strings and not as adresses;
#2. DO NOT use special characters, accents, or spaces when naming adresses, folders or excel files;
#3. DO NOT change the type of file that will be created, or the file you will get will not be an Excel file ('.xlsx').

#===NOTAS===#
# 1. NO elimine la 'r' antes de la carpeta de búsqueda y guarde las direcciones de la carpeta, o el archivo reconocerá las direcciones como cadenas y no como índices;
#2. NO use caracteres especiales, acentos o espacios al nombrar índices, carpetas o archivos de Excel;
# 3. NO cambie el tipo de archivo que se creará, o el archivo que obtendrá no será un archivo de Excel ('.xlsx').
