import random 
lista = []
for i in range(20):
    numero_aleatorio = random.randint(1,100)
    lista += [numero_aleatorio]
nova_lista_par = [x for x in lista if x%2 == 0]
nova_lista_impar = [x for x in lista if x%2 != 0]

print(nova_lista_par)
print(nova_lista_impar)