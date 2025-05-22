"""for contador in range (1,10):
    print (contador)
print("fim")"""
contador = 1
while contador < 10:
    print(contador)
    contador = contador + 1
print("FIM")
#outro exemplo
numero = 1
somapares = 0
somaimpares = 0
while numero != 0:
    numero = int(input("Digite um valor:"))
    if numero !=0:
        if numero % 2 == 0:
            somapares = somapares + 1
        else:
            somaimpares = somaimpares + 1
print ("Foram digitado {} numeros pares".format(somapares))
print ("Foram digitados {} numeros impares".format(somaimpares))
print ("O numero 0 foi digitado FIM")
#outro exemplo
resposta = "S"
while resposta == "S":
    numero = int(input("Digite um valor:"))
    resposta = str(input("Quer continuar? [s/n]")).upper()
print("FIM")
