numero_base = int(input("Digita ae:"))
resultado = numero_base

for i in range(numero_base-1, 0, -1):
    resultado *= i
    if i == numero_base - 1:
        print(f'{numero_base}!={numero_base}.{i}', end='.')
    elif i == 1:
        print(f'{i}', end='=')
    else:
        print(f'{i}', end='.')

print(resultado)

