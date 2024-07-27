base = int(input("Insira o valor da base:"))
expoente = int(input("Insira o valor do expoente:"))
multi = base

for i in range(0, expoente):
    base = multi * base
print(base)