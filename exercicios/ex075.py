numero = (int(input("Digite um numero:")),
            int(input("Digite um numero:")),
            int(input("Digite um numero:")),
            int(input("Digite um numero:")))
print (f"O numero 9, aparece {numero.count(9)} vezes")
if 3 in numero:
    print (f"O numero 3, aparece na {numero. index(3)+1} posição")
else:
    print  ("O numero 3, não foi digitado pelo usuario!")
print ("Os numeros pares digitados foi: ", end= "")
for contador in numero:
    if contador % 2 == 0:
        print (contador, end= " ")
