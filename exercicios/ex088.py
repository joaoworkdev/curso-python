from random import randint
from time import sleep
lista = list()
jogos = list()
print("-" * 30)
print("      JOGA NA MEGA SENA     ")
print("-" * 30)
quantidade = int(input("Quantos jogos você quer jogar?"))
total = 1
while total <= quantidade:
    conte = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            conte += 1
        if conte >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print("-=" * 3, f" SORTEANDO {quantidade} JOGOS ", "-=" * 3)
for indice , l in enumerate(jogos):
    print(f"Jogo {indice + 1} : {l} ")
    sleep(1)
print("-=" * 5, "< BOA SORTE! >", "-=" * 5)
