import string
import random
lista = []
vogais = ['a', 'e', 'i', 'o', 'u',]
vogais_uppercase = ['A', 'E', 'I', 'O', 'U',]
consoantes = 0
for i in range(10):    
    ascii_letters = string.ascii_letters
    random_letter = random.choice(ascii_letters)
    lista += [random_letter]
    if random_letter not in vogais and random_letter not in vogais_uppercase:
        consoantes += 1
        print(random_letter, end=',')