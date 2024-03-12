#Estrutura de repetição
##Executa uma instrução várias vezes

#For crescente
for i in range(0, 10):
    print(i, "repetições")

#for decrescente: range(inicio, fim-1, passo)
for i in range(10, -1,-2):
    print(i, "repetição decrescente")

#for com lista
lista_nomes = ['Nathan', 
               'Gabriel', 
               'Kaique', 
               'Neymar']
for nome in lista_nomes:
    print(nome)

#imprime os indices com seus valores
for index, nome in enumerate(lista_nomes):
    print(index," -> ", nome)


