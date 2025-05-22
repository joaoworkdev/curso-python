numeros = list()
for contador in range(0,5):
    valor = int(input("Digite um valor:"))
    if contador == 0 or valor > numeros[-1]:
        numeros.append(valor)
    else:
        posicao = 0
        while posicao < len(numeros):
            if valor <= numeros[posicao]:
                numeros.insert(posicao, valor)
                break
            posicao = posicao + 1

numeros.sort()
print(numeros)
