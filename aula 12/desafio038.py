numero1 = int(input("Dugute um numero:"))
numero2 = int(input("Digite outro numero:"))
if numero1 > numero2:
    print ("O primeiro valor {} é maior".format(numero1))
elif numero1 < numero2:
    print ("O segundo valor {} é maior".format(numero2))
else:
    print ("Não existe valor maior, os dois são iguais")