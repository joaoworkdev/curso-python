
while True:
    numero = int(input("Quero ver a tabuada de:"))
    if numero < 0:
        break
    for contador in range (1,11):
        resultado = numero * contador
        print (f"{numero} X {contador} = {numero * contador}")
print ("TABUADA ENCERRADA")