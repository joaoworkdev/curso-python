numero = int(input("Digite o numero de inicio:"))
numero2 = int(input("Digite a razão:"))
decimo = numero + (10 -1) * numero2
for contador in range(numero, decimo + numero2 ,numero2):
    print (contador)