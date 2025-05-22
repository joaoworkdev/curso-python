numero = int(input("Digite um numero:"))
total = 0 
for contador in range(1,numero + 1):
    if numero % contador == 0:
        print (end= " ")
        total = total + 1
    else:
        print(end= " ")
    print (contador, end=" ")
if total == 2:
    print ("Numero é primo")
else:
    print ("Numero não e primo")
