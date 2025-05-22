menor = 0
maior = 0
for contador in range(1,5+1):
    peso = float(input("Digite o peso:"))
    if contador == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print ("Menor peso é {}".format(menor))
print ("Meior peso é {}".format(maior))