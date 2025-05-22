def ficha(nome="", gols=0):

    if nome == "":
        nome = "desconhecido"
    if gols == "":
        gols = 0

nome = str(input("Nome do jogador: "))
gols = int(input("Quantidade de gols: "))
print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")
