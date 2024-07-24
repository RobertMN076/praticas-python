#Esse enunciado tem um erro.

pais_a = 80000
pais_b = 200000
anos = 0
porcentagem_a = pais_a * 3 / 100
porcentagem_b = pais_b * 1 / 100


while pais_a < pais_b:
    anos += 1
    pais_a += porcentagem_a
    pais_b += porcentagem_b
    print(anos)
