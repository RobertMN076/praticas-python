import random
lista = []
for i in range(4):
    notas = random.randint(0, 10)
    lista += [notas]

soma = lista[0] + lista[1] + lista[2] + lista[3]
media = soma / 4
print(lista)
print(media)