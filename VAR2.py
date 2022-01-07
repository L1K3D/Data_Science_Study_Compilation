#===DECLARAÇÃO DAS BIBLIOTECAS USADAS===#
#===LIBRARY STATEMENT===#
#===DECLARACIÓN DE BIBLIOTECA===#
import glob
import pandas as pd
from openpyxl import Workbook

#===PROCESSO DE LOCALIZAÇÃO DAS PASTAS E DA LEITURA DOS ARQUIVOS===#
#===LOCALIZATION OF FOLDER ADRESSES WHERE THE EXCEL FILES ARE===#
#===UBICACIÓN DE CARPETAS Y PROCESO DE LECTURA DE ARCHIVOS===#
dados1 = glob.glob(r'Enter first folder adress\*.xlsx')
print (dados1)
dados2 = glob.glob(r'Enter second folder adress\*.xlsx')
print(dados2) 

#===CRIAÇÃO DAS DUAS TABELAS ONDE OS DADOS CONSOLIDADOS FICARÃO GRAVADOS===#
#===CREATING THE VARIABLES OF DATA CONSOLIDATION===#
#===CREACIÓN DE DOS TABLAS DONDE SE REGISTRARÁN LOS DATOS CONSOLIDADOS===#
total_dados1 = pd.DataFrame()
total_dados2 = pd.DataFrame()

#===SISTEMA DE UNIÃO DE TODOS OS ARQUIVOS EXCEL DA PASTA NÚMERO 1===#
#===SISTEM OF PROCESS AND UNION OF ALL EXCEL FILES PRESENT IN FOLDER NUMBER 1===#
#===UNIR AL SISTEMA DE TODOS LOS ARCHIVOS DE EXCEL EN LA CARPETA NÚMERO 1===#
for item1 in dados1:
    tabela1 = pd.read_excel(item1)
    total_dados1 = pd.concat([total_dados1, tabela1], axis=0, ignore_index = True)
    total_dados1.head()
print(total_dados1)
print(total_dados1.shape)

#===SISTEMA DE UNIÃO DE TODOS OS ARQUIVOS EXCEL DA PASTA NÚMERO 2===#
#===SISTEM OF PROCESS AND UNION OF ALL EXCEL FILES PRESENT IN FOLDER NUMBER 2===#
#===UNIR AL SISTEMA DE TODOS LOS ARCHIVOS DE EXCEL EN LA CARPETA NÚMERO 2===#
for item2 in dados2:
    tabela2 = pd.read_excel(item2)
    total_dados2 = pd.concat([total_dados2, tabela2], axis=0, ignore_index = True)
    total_dados2.head
print(total_dados2)
print(total_dados2.shape)

#===CRIAÇÃO DO ARQUIVO EXCEL CONSOLIDADO===#
#===CREATING THE CONSOLIDATED EXCEL FILE===#
#===CREACIÓN DEL ARCHIVO CONSOLIDADO EXCEL===#
df_final = pd.DataFrame()
df_final = pd.concat([total_dados1, total_dados2], axis=0, ignore_index=True)
print(df_final)
print(df_final.shape)

#===SALVAMENTO DO ARQUIVO EXCEL CONSOLIDADO===#
#===SAVING THE FINAL EXCEL FILE===#
#===GUARDAR EL ARCHIVO EXCEL CONSOLIDADO===#
df_final.to_excel(r'Enter folder adress\Enter file name.xlsx')

