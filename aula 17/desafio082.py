pares = list()
impares = list()
numeros = list()
numero = 0
while True:    
    numero = int(input("Digite um numero:"))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    resp = str(input("Voce quer continuar? [S/N]")).upper().strip()
    if resp != "S":
        break

print(f"Os numeros digitados pelo usuario são: {numeros}")
print(f"Os numeros pares são: {pares}")
print(f"Os numeros impares são {impares}")
