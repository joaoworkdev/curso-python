digitados = 0
numero = 0
soma = 0
numero = int(input("Digite um valor:"))
while numero != 999:
    digitados = digitados + 1
    soma = soma + numero
    numero = int(input("Digite um valor:"))
print ("Foram digitados {} numeros, e a soma entre eles é {}".format(digitados, soma))