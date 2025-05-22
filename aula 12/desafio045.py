from random import randint
itens = ("Pedra","Papel", "Tesoura")
computador = randint(0,2)
print ("""SUAS OPÇÕES:
       [0] PEDRA
       [1] PAPEL
       [2] TESOURA""")
resposta = int(input("Qual sua jogada:"))
print ("-=" * 11)
print ("O computador escolheu {}".format(itens[computador]))
print ("O jogador escolheu {}".format(itens[resposta]))
print ("-=" * 11)
if computador == 0: 
    if resposta == 0:
        print ("EMPATE")
    elif resposta == 1:
        print ("Voce ganhou")
    elif resposta == 2:
        print ("Voce perdeu")
    else:
        print ("JOGADA INVALIDA")
elif computador == 1:
    if resposta == 0:
        print ("Voce perdeu")
    elif resposta == 1:
        print ("Empate")
    elif resposta == 2:
        print ("Voce ganhou")
    else:
        print ("JOGADA INVALIDA")
elif computador == 2:
    if resposta == 0:
        print ("Voce ganhou")
    elif resposta == 1:
        print ("Voce perdeu")
    elif resposta == 2:
        print ("Empate")
    else:
        print ("JOGADA INVALIDA")
        
