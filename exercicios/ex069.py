resp = "S"
idade = mais18 = homens = mulheres = 0
sexo = " "
while True:
    idade = int(input("Digite sua idade:"))
    sexo = str(input("Digite seu sexo: [M/F]")).upper().strip()[0]
    if idade > 18:
        mais18 = mais18 + 1
    if sexo == "M":
        homens = homens + 1
    else:
        if idade < 20:
            mulheres = mulheres + 1
    resp = str(input("Voce quer continuar?")).upper().strip()[0]
    if resp == "N": 
        break
print (f"Foram cadastradas {mais18} pessoas com mais de 18 anos ")
print (f"Foram cadastrados {homens} pessoas com sexo masculino")
print (f"Foram cadastradas {mulheres} mulheres com menos de 20 anos")