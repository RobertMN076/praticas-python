import random
# numero = random.randint(1,100)
numero = int(input("digita ae"))
antecessor = 0
sequencia = 1

print(sequencia, end=",")

for i in range(0,numero):
    proximo = antecessor + sequencia
    if proximo > 500:
        break
    else:
        print(proximo, end=",")
        antecessor = sequencia
        sequencia = proximo