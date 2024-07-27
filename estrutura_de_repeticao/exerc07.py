import random
maior_numero = 0

for i in range(0, 5+1):
    numero = random.randint(1,100)
    if maior_numero < numero:
        maior_numero = numero
        print(maior_numero)