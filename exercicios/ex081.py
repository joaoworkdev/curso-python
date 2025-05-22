numeros = list()
while True:
    numeros.append(int(input("Digite um numero:")))
    resp = str(input("Voce quer continuar? [S/N]")).upper().strip()[0]
    if resp in "Nn":
        break

print(f"Voce digitou {len(numeros)} elementos")
numeros.sort(reverse=True)
print (f"Os valores digitados em ordem decrescentes são {numeros}")
if 5 in numeros:
    print ("O numero 5, faz parte da lista")
else:
    print("O numero 5, não faz parte da lista")
