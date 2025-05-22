numeros = list()
for contador in range(0,5):
    valor = int(input("Digite um valor:"))
    if contador == 0 or valor > numeros[-1]:
        numeros.append(valor)
        print("Adicionado ao final da lista")
    else:
        posicao = 0
        while posicao < len(numeros):
            if valor <= numeros[posicao]:
                numeros.insert(posicao, valor)
                print(f"Adicionado na posição {posicao} da lista")
                break
            posicao = posicao + 1
numeros.sort()
print (numeros)
