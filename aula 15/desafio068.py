import random
par = ""
impar = ""
resp = ""
ganhar = 0
while ganhar >= 0:
    computador = random.randint(0,10)
    numero = int(input("Digite um numero:"))
    resp = str(input("PAR OU IMPAR [P/I]")).upper().strip()[0]
    soma = computador + numero
    if resp == "P":
        if soma % 2 == 0:
            print (f"Voce jogou {numero} e o computador {computador}. Total de {soma} DEU par")
            print ("VOCE GANHOU!")
            ganhar = ganhar + 1
        else:
            print (f"Voce jogou {numero} e o computador {computador}. Total de {soma} DEU impar")
            print ("VOCE PERDEU!")
            break
    else:
        if soma % 2 == 0:
            print (f"Voce jogou {numero} e o computador {computador}. Total de {soma} DEU PAR")
            print ("VOCE PERDEU!")
            break
        else:
            print (f"Voce jogou {numero} e o computador {computador}. Total de {soma} DEU IMPAR")
            print ("VOCE GANHOU!")
            gamhar = ganhar + 1
print (f"GAMER OVER! voce venceu {ganhar} vezes.")