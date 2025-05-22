numeros = [[], []]
valores = 0

for c in range(0,7):
    valores = int(input("Digite um numero:"))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)

numeros[0].sort()
numeros[1].sort()

print(f"Os valores pares são {numeros[0]}")
print(f"Os valores impares são {numeros[1]}")