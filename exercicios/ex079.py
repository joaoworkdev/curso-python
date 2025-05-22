numeros = list()
while True:
    valor = int(input("Digite um numero:"))
    if valor not in numeros:
        numeros.append(valor)
        print("Numero adicionado com sucesso!")
    else:
        print ("Numero ja existe, não foi adicionado!")
    resp = str(input("Voce quer continuar?")).strip().upper()[0]
    if resp == "N":
        break
numeros.sort()
print(numeros)