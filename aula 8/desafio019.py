
from random import choice
nome1 = str(input("Digite o primeiro nome:"))
nome2 = str(input("Digite o segundo nome:"))
nome3 = str(input("Digite o terceiro nome:"))
nome4 = str(input("Digite o quarto nome:"))
nomes = [nome1,nome2,nome3,nome4]
escolhido = choice(nomes)
print ("O nome escolhido é {}".format(escolhido))
