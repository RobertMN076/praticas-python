import random

soma = 0
inicio = random.randint(1,100)
final = random.randint(1,100)

while inicio == final:
    inicio = random.randint(1,100)
    final = random.randint(1,100)

for i in range(inicio, final+1):
    print(i)
    soma += i