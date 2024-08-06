import random

lista = []
for i in range(1,31):
    numero = random.randint(1,10)
    lista += [numero ** 2]
print(lista)

nova_lista = [i+i for i in lista]
print(nova_lista)

