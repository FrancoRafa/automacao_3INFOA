import pandas as pd
from main import cadastrar

#ler planilha
plan = pd.read_excel("Dados.xlsx")

#Dados de cada linha 
for index, linha in plan.iterrows():
    cadastrar(linha['Atleta'], linha['Modalidade'], linha['Medalha'], linha['Comitê'] )
    


