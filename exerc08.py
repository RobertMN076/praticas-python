import random
soma = 0

for i in range(0, 5+1):
    numero = random.randint(1,100)
    soma += numero
media = soma/5
print(f'A soma dos números gerados foi {soma}. E a média foi {media}.')