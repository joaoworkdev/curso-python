anonasci = int(input("Qual ano de nascimento?"))
alistar = 2006
idade = 2024 - anonasci
if anonasci > 2006:
    print ("Deverá se alistar, voce possui {} anos".format(idade))
    print ("Falta {} anos para se alistar".format(18 - idade))
elif anonasci == alistar:
    print ("Esá no tempo de alistar, voce tem {}".format(idade))
else:
    print ("Já passou o tempo de se alistar, voce tem {}".format(idade))
    print ("Já passou {} anos do prazo de se alistar".format(idade - 18))


