numeros = list()
while True:
    valor = int(input("Digite um valor:"))
    if valor not in numeros:
        numeros.append(valor)
        print("Numero adicionado com sucesso!")
    else:
        print("Numero duplicado. Não sera adicionado")
    resposta = str(input("Voce quer continuar? [S/N]")).upper().strip()[0]
    if resposta == "N":
        break
numeros.sort()
print(numeros)