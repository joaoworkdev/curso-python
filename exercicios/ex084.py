temporaria = list()
primaria = list()
maior = menor = 0
while True:
    temporaria.append(str(input("Digite seu nome:")))
    temporaria.append(float(input("Digite seu peso:")))
    if len(primaria) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]

    primaria.append(temporaria[:])
    temporaria.clear()

    resp = str(input("Voce quer continuar? [S/N]"))
    if resp in "Nn":
        break

print(f"Foram cadastradas ao total {len(primaria)} pessoas.")
print(f"O maior peso cadastrado foi {maior}. Peso de ", end="")
for cadapessoa in primaria:
    if cadapessoa[1] == maior:
        print(f"[{cadapessoa[0]}]", end= "")
print()
print(f"O menor peso cadastrado foi {menor}. Peso de ", end="")
for cadapessoa in primaria:
    if cadapessoa[1] == menor:
        print(f"[{cadapessoa[0]}]", end= "")
