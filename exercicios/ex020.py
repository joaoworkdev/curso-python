from random import shuffle
nome1 = input("Primeiro aluno:")
nome2 = input("Segundo aluno:")
nome3 = input("Terceiro aluno:")
nome4 = input("Quarto aluno:")
sorteio = [nome1,nome2,nome3,nome4]
shuffle(sorteio)
print ("A ordem sorteada foi:")
print (sorteio)
