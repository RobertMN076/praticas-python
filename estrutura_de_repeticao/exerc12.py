numero = int(input("Escolha o número que deseja ver a tabuada:"))
tabuada = 0

for i in range(0, 10+1):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")