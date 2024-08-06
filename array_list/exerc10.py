import random

lista = []
segunda_lista = []
terceira_lista = []

for i in range(1,31):
    if len(lista) != 10:
        numero = random.randint(1,10)
        lista += [numero ** 2]
    elif len(segunda_lista) != 10:
        numero = random.randint(1,10)
        segunda_lista += [numero ** 2]
    else:
        numero = random.randint(1,10)
        terceira_lista += [numero ** 2]

nova_lista = [i+i for i in lista]
segunda_nova_lista = [i+i for i in segunda_lista]
terceira_nova_lista = [i+i for i in terceira_lista]

print(nova_lista)
print(segunda_nova_lista)
print(terceira_nova_lista)