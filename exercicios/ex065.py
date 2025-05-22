resposta = "S"
numero = quantidade = soma = media = maior = menor = 0
while resposta != "N".upper():
    numero = int(input("Digite um numero:"))
    quantidade = quantidade + 1
    soma = soma + numero
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input("Voce quer continuar? [S/N]")).upper().strip()[0]
media = soma / quantidade
print ("O maior valor digitado foi {}".format(maior))
print ("O menor valor digitado foi {}".format(menor))
print ("Foram digitados {} numeros, e a media entre eles é {}".format(quantidade,media))