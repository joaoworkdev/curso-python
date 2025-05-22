numeros = list()
maior = 0
menor = 0
for cont in range(0,5):
    numeros.append(int(input(f"Digite um valor para a posição {cont}:")))
    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]

print(f"Os valores da lista é {numeros}")
print (f"O maior valor digitado foi {maior} na posição ", end="")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} na posição ", end="")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"{i}...", end="")
print()