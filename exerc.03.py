verificaçao_civil = ["solteiro", "casado", "viúvo", "divorciado"]
verificaçao_sexo = ["masculino", "feminino"]


while True:
    nome = input('Digite seu nome:')
    if len(nome) >= 3:
        break
    else:
        print('O nome deve ter pelo menos 3 letras.')

idade = int(input('Digite sua idade:'))
while idade < 0 or idade > 150:
    print('Digite uma idade válida')
    idade = int(input('Digite sua idade:'))
 
salario = int(input('Digite seu salario:'))
while salario < 0:
    print('Digite um salário válido')
    salario = int(input('Digite seu salario:'))

sexo = input('Digite seu sexo:')
while sexo not in verificaçao_sexo:
    print('Digite um sexo válido')
    sexo = input('Digite seu sexo:')

estado_civil = input('Digite seu estado civil:')
while estado_civil not in verificaçao_civil:
    print('Digite um estado civil válido')
    estado_civil = str(input('Digite seu estado civil:'))

print(f'Programa encerrado, os resultados foram {nome}, {idade}, {salario}, {sexo}, {estado_civil}')




