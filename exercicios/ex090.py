aluno = dict()
aluno["Nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Media de {aluno["Nome"]}: "))
if aluno["media"] >= 7:
    aluno["situação"] = "APROVADO"
elif aluno["meida"] >= 5:
    aluno["situação"] = "RECUPERAÇÃO"
else:
    aluno["situação"] = "REPROVADO"

for k, v in aluno.items():
    print(f"{k} é igual a {v}")
    