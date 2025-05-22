from random import randint 
computador = randint (0,10)
print ("Pensei em um numero de 0 a 10")
print ("Será que voce consegue adivinha qual é?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite?"))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("O numero é menos")
        else:
            print ("O numero é mais")
print ("Acertou com {} tentativas!".format(palpites))
