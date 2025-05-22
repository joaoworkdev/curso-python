resp = "S"
soma = 0
media = 0
numero = 0
somanumero = 0
menor = 0
maior = 0
while resp != "N".upper(): 
    numero = int(input("Digite um valor:"))
    soma = soma + 1
    somanumero = somanumero + numero
    if soma == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input("Voce quer continuar?[S/N]")).upper().strip()[0]
media = somanumero / soma 
print ("A media dos valores e {}".format(media))
print ("O maior numero digitado foi {}".format(maior))
print ("O menor numero digitado foi {}".format(menor))