pessoas = dict()
cadastro = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas["nome"] = str(input("NOME: "))
    while True:
        pessoas["sexo"] = str(input("Sexo: [M/F]")).upper()[0]
        if pessoas["sexo"] in "MF":
            break
        else:
            print("ERRO! Por favor, digite apenas M ou F")
    pessoas["idade"] = int(input("IDADE: "))
    soma += pessoas["idade"]
    cadastro.append(pessoas.copy())
    while True:
        resp = str(input("Quer continuar ? [S/N]")).upper()[0]
        if resp in "SN":
            break
        else:
            print("ERRO! Respnda apenas S ou N. ")
    if resp == "N":
        break
media = soma / len(cadastro)
print("-=" * 30)
print(f"Ao todo temos {len(cadastro)} pessoas cadastradas")
print(f"A média de idade de todas as pessoas é {media:5.2f}")
print("As mulheres cadastradas foram: ", end="")
for p in cadastro:
    if p["sexo"] == "F":
        print(f"{p["nome"]} ", end="")
print()
print("Lista das pessoas que estão acima da média ", end="")
for p in cadastro:
    if p["idade"] >= media:
        print("     ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()
print("ENCERRADO")