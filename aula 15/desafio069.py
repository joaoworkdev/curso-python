resp = "S"
pessoas = 0
homens = 0
menos20 = 0
while resp == "S".upper().strip()[0]: 
    idade = int(input("Digite sua idade:"))
    sexo = str(input("Digite seu sexo [F/M]")).upper().strip()[0]
    pessoas = pessoas + 1
    if sexo == "M":
        homens = homens + 1
    elif sexo == "F":
        if idade < 20:
            menos20 = menos20 + 1
    resp = str(input("Voce quer continuar [S/N]")).upper().strip()[0]
    if resp != "S":
        break
print (f"Foram cadastradas {pessoas} pessoas")
print (f"Foram cadastrados {homens} homens")
print (f"Foram cadastradas {menos20} mulheeres com menos de 20 anos")