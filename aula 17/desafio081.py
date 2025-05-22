numeros = list()
while True:
    numeros.append(int(input("Digite um valor:")))
    resp = str(input("Voce quer continuar? [S/N]")).upper().strip()[0]
    if resp == "N":
        break

if 5 in numeros:
    print("O numero 5, se encotra na lista")
else:
    print("O numero 5 nao faz parte da lista")

numeros.sort(reverse=True)
print(numeros)
print(f"Foram digitados ao total {len(numeros)} elementos")
