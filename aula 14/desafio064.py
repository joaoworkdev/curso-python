digitados = 0
numero = 0
soma = 0
while numero != 999:
    numero = int(input("Digite um valor:"))
    if numero != 999:
        digitados = digitados + 1
        soma = soma + numero
    else:
        print ("Programa encerrado")
print ("Foram digitados {} numeros, e a soma entre eles é {}".format(digitados, soma))