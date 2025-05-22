aluno = {}
aluno["nome"] = str(input("Digite o nome do aluno:"))
aluno["media"] = float(input(f"Qual a média de {aluno["nome"]}: "))

if aluno["media"] >= 7:
    aluno["Situação"] = "APROVADO"
elif aluno["media"] >= 5:
    aluno["Situação"] = "RECUPERAÇÃO"
else: 
    aluno["Situação"] = "REPROVADO"

print(f"O aluno {aluno["nome"]} foi {aluno["Situação"]}")