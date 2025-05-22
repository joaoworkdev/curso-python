numeros = list()
maior = 0
menor = 0
for cont in range(0,5):
    numeros.append(int(input(f"Digite um valor na posição {cont}:")))
    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont] 

print(f"O maior valor é {maior}")
for indice, valor in enumerate(numeros):
    if valor == maior:
        print(f"{indice}", end="")
print(f"O menor valor é {menor}")
for indice , valor in enumerate(numeros):
    if valor == menor:
        print(f"{indice}", end="")
print(f"Os numeros da lista é {numeros}")