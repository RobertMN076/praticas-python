
lista = []
for i in range(1,6):
    if i > 1:
        lista = []
        idade = int(input('Digite sua idade: '))
        altura = float(input('Digite sua altura: '))
        lista += [idade, altura]
        print(f' A altura e a idade, respectivamente do candidato {i}: {lista[::-1]}')
    else:
        idade = int(input('Digite sua idade: '))
        altura = float(input('Digite sua altura: '))
        lista += [idade, altura]
        print(f' A altura e a idade, respectivamente do candidato {i}: {lista[::-1]}')