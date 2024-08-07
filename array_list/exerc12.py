import random
soma_mensal = 0
media_mensal = 0
for i in range(0,12):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for k in range(30):
        temperatura_dias = random.randint(1,40)
        soma_mensal += temperatura_dias
        if k == 30:
            media_mensal = soma_mensal/30
    print(f'A média mensal do mês {i} - {media_mensal}')