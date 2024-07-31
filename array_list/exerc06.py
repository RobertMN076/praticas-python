import random

lista = []
for i in range(5):
    numero_aleatorio = random.randint(1,100)
    lista += [numero_aleatorio]
nova_lista_soma = [x+x for x in lista]
nova_lista_multiplicacao = [x*x for x in lista]

print(f'A lista é: {lista}')
print(f'A nova lista com soma é: {nova_lista_soma}')
print(f'A nova lista com multiplicação é: {nova_lista_multiplicacao}')
