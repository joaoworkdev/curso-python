import random
nome1 = input("Primeiro aluno:")
nome2 = input("Segundo aluno:")
nome3 = input("Terceiro aluno:")
nome4 = input("Quarto aluno:")
alunos = [nome1,nome2,nome3,nome4]
random.shuffle(alunos)
print ("A ordem de apresentação sera:")
print (alunos)

