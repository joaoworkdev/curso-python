soma = 0
for contador in range (1,500+1,2):
    if contador % 3 == 0:
        soma = soma + contador
print ("A soma de impares de 1 a 500 é {}".format(soma))