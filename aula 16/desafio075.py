nove = 0
numero = (int(input("Digite um numero:")),
            int(input("Digite um numero:")),
            int(input("Digite um numero:")),
            int(input("Digite um numero:")))
print (f"Voce digitou os valores: {numero}")
print (f"O numero 9 apareceu {numero.count(9)} vezes")
if 3 in numero:
    print (f"O valor 3 apareceu na posição {numero.index(3)+1}")
else:
    print ("O valor 3, não foi digitado!")
print ("Os valores pares digitados foram ", end="")
for n in numero:
    if n % 2 == 0:
        print (n, end= " ")
