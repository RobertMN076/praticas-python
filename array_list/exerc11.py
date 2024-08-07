import random
altura_soma = 0
altura_lista = []
idade_lista = []
altura_geral = []
for i in range(1, 11):
    idade = random.randint(1,20)
    altura = float(input('Digite sua altura: '))
    idade_lista += [idade]
    altura_geral += [altura]
    altura_soma += altura
    if idade < 13:
        altura_lista += [altura]

for i in altura_geral:
    if i == altura_geral[9]:
        media_altura = altura_soma/10
        formatado = "{:.1f}" .format(media_altura)
        

for i in altura_lista:
    if i < media_altura:
        texto = 'A altura {} é menor que a média {:.1f}' .format(i, media_altura)
        print(texto) 