time = list()
jogador = {}
partidas = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input("Digite o nome:"))
    totalpartidas = int(input(f"Partidas do {jogador["nome"]}:"))
    partidas.clear()
    for contador in range(0,totalpartidas):
        partidas.append(int(input(f"Quantos gols na partida { contador + 1}: ")))

    jogador["gols"] = partidas[:]
    jogador["total gols"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Voce quer continuar? [S/N]")).upper()[0]
        if resp in "SN":
            break
        else:
            print("ERRO! Responda apenas S ou N. ")
    if resp == "N":
        break
print("-= " * 30)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-" * 30)
for k, v in enumerate(time):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end= "")
    print()
print("-" * 30)

while True:
    busca = int(input("Mostrar dados de qual jogador?"))
    if busca == 999:
        break
    if busca >= len(time):
        print("ERRO! não existe jogador com codigo da busca")
    else:
        print(f"  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:")
        for i, g in enumerate(time[busca]["gols"]):
            print(f"      No jogo {i+1} fez tantos {g} gols")
    print("-" * 40)
print("<< VOLTE SEMPRE >>")