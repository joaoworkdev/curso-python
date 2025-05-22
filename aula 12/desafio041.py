anonasci = int(input("ano de nascimento:"))
idade = 2024 - anonasci
print ("A idade do aluno é {}".format(idade))
if idade <= 9:
    print ("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade== 20: 
    print("SENIOR")
else:
    print("MASTER")