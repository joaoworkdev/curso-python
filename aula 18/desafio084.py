pessoas = list()
dados = list()
maior = menor = 0

while True:
    pessoas.append(str(input("Digite seu nome:")))
    pessoas.append(float(input("Digite seu peso:")))
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
        
    dados.append(pessoas[:])
    pessoas.clear()

    resp = str(input("Voce quer continuar? [S/N]")).upper().strip()[0]
    if resp == "N":
        break

print(f"Ao todo voce cadastrou {len(dados)} pessoas.")
print(f"O maior peso foi de {maior}Kg. Peso de ", end="")
for p in dados:
    if p[1] == maior:
        print(f"[{p[0]}]", end= "")
print()
print(f"O menor peso foi de {menor}Kg. Peso de ", end= "")
for p in dados:
    if p[1] == menor:
        print(f"[{p[0]}", end= "")
print()
