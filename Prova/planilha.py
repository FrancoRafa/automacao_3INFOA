import pandas as pd
from main import colocar

#ler planilha
plan = pd.read_excel("PlanilhaLancamento.xlsx")
print(plan)


nome_meu = plan[plan['Nome'].str.contains('RAFAELA GUIMARÃES FRANCO DA SILVA', case=False)]
print(nome_meu)


for index, linha in nome_meu.iterrows():
    colocar(linha['Nome'], linha['Nota'], linha['Atividade'], linha['Turma'] )
    




