
import random
numero = random.randint(1,100)
antecessor = 0
sequencia = 1

print(sequencia, end=",")

for i in range(0,numero):
    proximo = antecessor + sequencia
    print(proximo, end=",")
    antecessor = sequencia
    sequencia = proximo