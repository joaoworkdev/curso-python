numero = list()
pares = list()
impares = list()
while True:
    numero.append(int(input("Digite um valor:")))
    resp = str(input("Voce quer continuar??? [S/N]"))
    if resp in "Nn":
        break
for indice, valor in enumerate(numero):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    
print(f"A lista completa {numero}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")
