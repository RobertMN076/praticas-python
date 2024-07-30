r = 0
while True:
    r += 1
    operacao = ['soma', 'subtração', 'multiplicação', 'divisão', 'resto']
    if r >= 2:
        print('Seja bem vindo ao menu novamente!')
        operacao_escolhida = input('Qual operação deseja realizar? ')
    else:
        operacao_escolhida = input('Qual operação deseja realizar? ')
    if operacao_escolhida in operacao:
        primeira_linha = int(input('Quantas linhas terão as matrizes? '))
        primeira_coluna = int(input('Quantas colunas terão as matrizes? '))
        segunda_linha = primeira_linha
        segunda_coluna = primeira_coluna
        linha_resultado = primeira_linha
        coluna_resultado = primeira_coluna
        primeira_matriz = []
        segunda_matriz = []
        for i in range(primeira_linha):
            primeira_linha = []
            for j in range(primeira_coluna):
                primeiro_valor = int(input(f'Digite o valor que irá na posição {i}, {j}: '))
                primeira_linha += [primeiro_valor]
            primeira_matriz += [primeira_linha]
        for i in range(segunda_linha):
            segunda_linha = []
            for j in range (segunda_coluna):
                segundo_valor = int(input(f'Digite o valor que será irá na posição de {i}, {j}: '))
                segunda_linha += [segundo_valor]
            segunda_matriz += [segunda_linha]
        if operacao_escolhida == operacao[0]:
            matriz_resultado = []
            for i in range(linha_resultado):
                linha_resultado = []
                for j in range(coluna_resultado):
                    terceiro_valor = primeira_matriz[i][j] + segunda_matriz[i][j]
                    linha_resultado += [terceiro_valor]
                matriz_resultado += [linha_resultado]
            for linha_resultado in matriz_resultado:
                print(linha_resultado)
        elif operacao_escolhida == operacao[1]:
            matriz_resultado = []
            for i in range(linha_resultado):
                linha_resultado = []
                for j in range(coluna_resultado):
                    terceiro_valor = primeira_matriz[i][j] - segunda_matriz[i][j]
                    linha_resultado += [terceiro_valor]
                matriz_resultado += [linha_resultado]
            for linha_resultado in matriz_resultado:
                print(linha_resultado)
        elif operacao_escolhida == operacao[2]:
            matriz_resultado = []
            for i in range(linha_resultado):
                linha_resultado = []
                for j in range(coluna_resultado):
                    terceiro_valor = primeira_matriz[i][j] * segunda_matriz[i][j]
                    linha_resultado += [terceiro_valor]
                matriz_resultado += [linha_resultado]
            for linha_resultado in matriz_resultado:
                print(linha_resultado)
        elif operacao_escolhida == operacao[3]:
            matriz_resultado = []
            for i in range(linha_resultado):
                linha_resultado = []
                for j in range(coluna_resultado):
                    terceiro_valor = primeira_matriz[i][j] / segunda_matriz[i][j]
                    linha_resultado += [terceiro_valor]
                matriz_resultado += [linha_resultado]
            for linha_resultado in matriz_resultado:
                print(linha_resultado)
        else:
            matriz_resultado = []
            for i in range(linha_resultado):
                linha_resultado = []
                for j in range(coluna_resultado):
                    terceiro_valor = primeira_matriz[i][j] % segunda_matriz[i][j]
                    linha_resultado += [terceiro_valor]
                matriz_resultado += [linha_resultado]
            for linha_resultado in matriz_resultado:
                print(linha_resultado)
    else:
        print('Nenhum valor válido inserido, o programa está sendo encerrado.')
        break