numero_base = int(input("Digita ae:"))
resultado = numero_base
repeticoes = int(input('Quantas vezes deseja calcular o fatorial? '))

while numero_base < 0 or numero_base > 16:
    print('Número inválido')
    numero_base = int(input('Digita ae: '))

for n in range(1, repeticoes+1):
    m = n-1
    if n != m:
        resultado = numero_base
        print('')
        for i in range(numero_base-1, 0, -1):
            resultado *= i
            if i == numero_base - 1:
                print(f'{numero_base}!={numero_base}.{i}', end='.')
            elif i == 1:
                print(f'{i}', end='=')
            else:
                print(f'{i}', end='.')
        print(resultado)