'''
As funções permitem modularizar o código, dividir ele em partes menores que podem ser reaproveitadas.
Isso simplifica a condição.

Estrutura função em pyton

def nome_funcao(param1, param2, paramN):
    //algum código que a função faz 
    return saida_da_funcao valor_retornado


'''
#cria uma função que calcula a área do triângulo
def calculateTriangleArea(base, altura):
    area = (base * altura) / 2
    return area






#cria uma função que calcula a área do triângulo
def calculateSquareArea(lado, lado):
    area = (lado * lado) / 2
    return area
'''
#Exemplo 1: chamar função
area1 = calculateTriangleArea(100, 10)
print("A área do triângulo 1 é ", area1)


#Exemplo 2: Chamar o função novamente
base = float(input('Digite a base: '))
altura = float(input('Digite a altura: '))
area2 = calculateTriangleArea(base, altura)
print("A área do triângulo 2 é ", area2)
'''