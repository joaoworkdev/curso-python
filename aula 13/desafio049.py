numero = int(input("Digite um numero para a tabuada:"))
for contador in range(0,10+1):
    multi = numero * contador
    print (numero,"X", contador, "= {}".format(multi))