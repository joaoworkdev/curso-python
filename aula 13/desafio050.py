soma = 0
for contador in range(1,6+1):
    numero = int(input("Digite um numero inteiro:"))
    if numero % 2 == 0:
        soma = soma + numero
print ("A soma dos numeros pares é:{}".format(soma))
