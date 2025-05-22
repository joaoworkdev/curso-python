jogador = {}
partidas = list()
jogador["nome"] = str(input("Digite o nome:"))
totalpartidas = int(input(f"Partidas do {jogador["nome"]}:"))

for contador in range(0,totalpartidas):
    partidas.append(int(input(f"Quantos gols na partida { contador + 1}: ")))

jogador["gols"] = partidas[:]
jogador["total gols"] = sum(partidas)
print("-=" * 30)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * 30)
print(f"O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.")
for i, v in enumerate(jogador["gols"]):
    print(f" =>    na partida {i + 1}, fez {v} gols.")
print(f"Foi um total de {jogador["total gols"]} gols.")
