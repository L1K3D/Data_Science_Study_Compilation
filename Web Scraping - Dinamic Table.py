#===1. IMPORTING LIBRARIES===
#===1. IMPORTANDO BIBLIOTECAS===
from cgitb import html
from lib2to3.pgen2 import driver
from unicodedata import numeric
from numpy import number, quantile
import selenium
import pandas as pd
import time
import datetime
from datetime import datetime, date, timedelta
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from webdriver_manager.chrome import ChromeDriverManager

#===2. DECLARING VARIABLES OF 'URL' AND GETTING THE DRIVE SET FOR THE RIGHT INTERNET BROWSER===
#===2. DECLARANDO AS VARIAVEIS DE 'URL' E CONFIGURANDO E CAPTURANDO O DRIVE SET CORRETO PARA O NAVEGADOR===
url = "Enter the url adress"

option = Options()
option.headless = True
#2.1. IN MY CASE, I USE THE GOOGLE CHROME AND I HAD TO FORCE THE PATH INSTALATION OF THE BROWSER IN THE CONNECTION WITH MY SCRIPT (I REALLY DON'T KNOW WHY THE SIMPLE WAY DOESN'T WORK, SO I HAVE TO DO THIS)
#2.1. NO MEU CASO, EU UTILIZEI O GOOGLE CHROME E TIVE DE FORÇAR A CONEXÃO ENTRE O MEU SCRIPT E O PATH ONDE O CHROME ESTAVA INSTALADO NO MEU COMPUTADOR (EU REALMENTE NÃO SEI PORQUE O JEITO SIMPLES DE CONEXÃO NÃO FUNCIONOU, ENTÃO EU TIVE DE FAZER ISSO)
drive = webdriver.Chrome(ChromeDriverManager().install())

drive.get(url)
time.sleep(10)

#2.2. ON THIS MOMENT, I HAD TO FIND THE PARTITION WHERE THE TABLE IS LOCATE AND DESCRIBE THE CLASS OF IT
#2.2. NESSE MOMENTO EU TIVE DE DECLARAR A PARTIÇÃO ONDE A TABELA ESTÁ LOCALIZADA E DESCREVER A SUA CLASSE
element = drive.find_element_by_xpath("//div[@class='table-responsive']//table")
html_content = element.get_attribute('outerHTML')

#===3. GETTING THE HOLE BODY DESCRIPTION OF THE HTML ADRESS SO THE SCRIPT CAN ONLY READ AND SELECT ELEMENTS WITH 'table' IN THE HEAD===
#===3. CAPTURANDO TODO O CORPO DESCRITIVO DO HTML E LENDO SOMENTE ELEMENTOS QUE TENHAM A SENTENÇA 'table' EM SUA DESCRIÇÃO===
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

#===4. ASSINGNING THE HTML ADRESS AND THE CLASS 'table' BEFORE GOT TO A DATAFRAME===
#===4. ATRIBUINDO O ENDEREÇO HTML E A CLASSE 'table' ANTES LIDA A UM DATAFRAME===
new_table = pd.read_html(str(table))[0].head(1)

#===5. ASSINGNING THE READER HTML VARIABLE TO A DATAFRAME TO BETTER DATA MANIPULATION===
#===5. ATRIBUINDO A VARIAVEL DE LEITURA DO HTML A UM DATAFRAME PARA MELHOR MANIPULAÇÃO DOS DADOS===
newdf = pd.DataFrame()
newdf = pd.concat([new_table])
