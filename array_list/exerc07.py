import random 

lista = []
for a in range(0,11):
    aluno = 1 + a
    for n in range(4):
        nota = random.randint(1, 100)
        lista += [nota]
        if n == 3:
            soma = lista[0] + lista[1] + lista[2] + lista[3]
            media = soma / 4
            print(f'A média do aluno {a} é: {media}')
            lista = []