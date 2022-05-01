'''
Desafio
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y.
Para cada X e Y, escreva uma mensagem para indicar se tais valores foram digitados em ordem crescente ou decrescente.

Entrada
A entrada é composta por vários casos de teste. Cada caso contém dois valores inteiros: X e Y.
A leitura deve ser encerrada caso sejam fornecidos os mesmos valores para X e Y.

Saída
Caso os valores tenham sido digitados na ordem crescente, imprima “Crescente”. No contrário, “Decrescente”.
'''

X = []
Y = []
cont = 0
n = True

while n:
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if a == b:
        n = False
        cont -= 1
    else:
        X.append(a)
        Y.append(b)
    cont += 1

i = 0
while i < cont:
    if X[i] > Y[i]:
        print('Decrescente')
    elif X[i] < Y[i]:
        print('Crescente')
    i += 1
