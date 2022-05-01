'''

Desafio
Você terá o desafio de ler um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma loja, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.


'''

valorTempoSegundos = int(input())

horas = valorTempoSegundos // 3600
minutos = (valorTempoSegundos % 3600) // 60
segundos = (valorTempoSegundos % 3600) % 60


print(f'{horas}:{minutos}:{segundos}')