soma = 0
velho = 0
mulheres = 0
homem = 0
for contador in range(1,4+1):
    nome = str(input("Digite seu nome:"))
    idade = int(input("Digite sua idade:"))
    sexo = str(input("Digite seu sexo:"))
    if sexo == "M":
        homem = homem + 1
        if idade > velho:
            velho = idade 
            nomevelho = nome 
    if sexo == "F" and idade < 20:
        mulheres = mulheres + 1
    soma = soma + idade
media = soma / 4
print ("Total de mulheres com menos de 20 anos é {}".format(mulheres))
print ("O nome do homem mais velho é {}".format(nomevelho))
print ("A média de idade é {}".format(media))