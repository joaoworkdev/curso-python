from random import randint
vitoria = 0
while True:
    jogador = int(input("Digite um valor:"))
    computador = randint(0,10)
    total = jogador + computador
    parouimpar = " "
    while parouimpar not in "PI":
        parouimpar = str(input("Par ou impar: [P/I]")).upper().strip()[0]
    print (f"Voce jogou {jogador} e o computador {computador}, somados = {total}")
    if total % 2 == 0:
        print ("DEU PAR")
    else:
        print ("DEU IMPAR")
    if parouimpar == "P":
        if total % 2 == 0:
            vitoria = vitoria + 1
            print ("Voce ganhou!")
        else:
            print ("Voce Perdeu")
            break
    elif parouimpar == "I":
        if total % 2 == 0:
            print ("Voce Perdeu")
            break
        else:
            vitoria = vitoria + 1
            print ("Voce ganhou!")
print (f"GAMER OVER! Voce venceu {vitoria} vezes.")