from random import randint
from time import sleep
numero = randint(0,5)
jogador = int(input("Tente adivinha o numero que estou pensando:"))
print ("PROCESSANDO...")
sleep(0.5)
if numero == jogador:
    print ("VOCÇÊ ACERTOU... PARABENS!")
else:
    print ("ERROU...Pensei em {} e não no {}".format(numero, jogador))
