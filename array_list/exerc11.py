import random

altura_lista = []
lista = []
for i in range(1, 11):
    idade = random.randint(1,20)
    altura = float(input('Digite sua altura: '))
    lista += [idade, altura]
    altura_lista += [altura]
    


soma = 0
for i in altura_lista:
    soma += i
    if i == altura_lista[9]:
        media_altura = soma/10
formatado = '{:.1f}' .format(media_altura)
print(formatado)
