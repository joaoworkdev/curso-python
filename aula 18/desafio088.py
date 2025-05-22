from random import randint
from time import sleep
lista = list()
jogos = list()
print("-" * 30)
print("          JOGA NA MEGA SENA        ")
print("-" * 30)
quant = int(input("Quantos jogos voce quer que eu sorteie?"))
total = 1
while total <= quant:
    conte = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            conte += 1
        if conte >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print("-=" * 3, f"SORTEANDO {quant} JOGOS ", "-=" * 3)
for i, l in enumerate(jogos):
    print(f"Jogos {i + 1}: {l}")
    sleep(1)
print("-=" * 5, "< BOA SORTE! >", "-=" * 5)