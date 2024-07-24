import random
par = 0
impar = 0

for i in range(0,10+1):
    numero_solicitado = random.randint(1,100)
    if numero_solicitado % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"A quantidade de números pares foram {par} e números ímpares foram {impar}.") 