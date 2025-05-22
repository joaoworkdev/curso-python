import random 
computador = random.randint(0,10)
numero = 0
tentativa = 0
while numero != computador:
    numero = int(input("Digite um numero:"))
    if numero == computador:
        print ("Voce acertou, parabens!")
    else:
        print ("Voce errou")
        tentativa = tentativa + 1
print ("O numero que o computador pensou foi {}, e voce tetnou {} vezes".format(computador, tentativa))
