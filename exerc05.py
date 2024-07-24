pais_a = int(input('Digite a população da sua cidade:'))
pais_b = int(input('Digite a população da cidade vizinha: '))
anos = 0
porcentagem_a = float(input('digite a porcentagem de crescimento anual:'))
porcentagem_b = float(input('digite a porcentagem de crescimento anual da cidade vizinha:')) 
calculo_a = pais_a * porcentagem_a/100
calculo_b = pais_b * porcentagem_b/100
intervalo_de_anos = int(input('Insira o intervalo de tempo:'))

for i in range(0, intervalo_de_anos+1):
    pais_a += calculo_a
    pais_b += calculo_b
print(f'A população do país A será de {pais_a} e a população do país B será de {pais_b} em {intervalo_de_anos} anos.')
