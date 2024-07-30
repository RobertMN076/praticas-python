import random
maior_valor = 0
menor_valor = 100
soma = 0

for i in range(1,6):
    numero = random.randint(0,100)
    soma += numero
    if numero > maior_valor:
        maior_valor = numero
    if menor_valor > numero:
        menor_valor = numero
print(f'O maior valor foi {maior_valor}, o menor valor foi {menor_valor} e a soma foi {soma}.')
