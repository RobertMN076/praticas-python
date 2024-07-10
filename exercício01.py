num = int(input('Digite um numero entre 0 e 10:'))

while num < 0 or num > 10:
    print('valor inválido')
    num = int(input('Digite outro número:'))
print('Valor válido, programa encerrado.')


          