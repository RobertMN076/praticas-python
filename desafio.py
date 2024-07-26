numero_fornecido = int(input('digita ae:'))

if numero_fornecido > 0 and numero_fornecido < 4:
    print('I' *numero_fornecido)
elif numero_fornecido == 4:
    print('IV')
elif numero_fornecido>=5 and numero_fornecido<9:
    auxiliar = numero_fornecido - 5
    print('V', end="")
    print('I' *auxiliar)
elif numero_fornecido == 9:
    print('IX')
elif numero_fornecido>=10 and numero_fornecido <= 39:
    print()
