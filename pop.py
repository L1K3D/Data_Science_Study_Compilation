import glob
import pandas as pd
from openpyxl import Workbook

dados1 = glob.glob(r'C:\Users\heitor\Desktop\Program\Teste\*.xlsx')
print (dados1)
dados2 = glob.glob(r'C:\Users\heitor\Desktop\Heitor\Teste2\*.xlsx')
print(dados2) 

wb = Workbook()
total_dados1 = pd.DataFrame()
total_dados2 = pd.DataFrame()

for item1 in dados1:
    tabela1 = pd.read_excel(item1)
    total_dados1 = pd.concat([total_dados1, tabela1], axis=0, ignore_index = True)
    total_dados1.head()
print(total_dados1)
print(total_dados1.shape)

#=============================#
for item2 in dados2:
    tabela2 = pd.read_excel(item2)
    total_dados2 = pd.concat([total_dados2, tabela2], axis=0, ignore_index = True)
    total_dados2.head
print(total_dados2)
print(total_dados2.shape)

#============================#
df_final = pd.DataFrame()
df_final = pd.concat([total_dados1, total_dados2], axis=0, ignore_index=True)
print(df_final)
print(df_final.shape)

#===========================#
df_final.to_excel(r'C:\Users\heitor\Desktop\Program\Teste.xlsx')

