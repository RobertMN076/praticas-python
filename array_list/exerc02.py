import random
lista = []
for i in range(6):
    numero_aleatorio = random.randint(1,101)
    lista += [numero_aleatorio]
print(lista[::-1])
print(lista)