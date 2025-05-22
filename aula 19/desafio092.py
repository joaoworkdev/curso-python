from datetime import datetime
anoatual = datetime.now().year
cadastro = {}

cadastro["nome"] = str(input("Digite seu nome:"))
cadastro["idade"] = int(input("ano de nascimento:"))
cadastro["ctps"] = int(input("Carteira de trabalho:"))

cadastro["idade"] = anoatual - cadastro["idade"]

if cadastro["ctps"] != 0:
    cadastro["ano"] = int(input("Ano de contratação: "))
    cadastro["salario"] = float(input("Salário:"))
    tempotrabalhado = anoatual - cadastro["ano"]
    tempoaposentar = 35 - tempotrabalhado
    cadastro["aposentar"] = tempoaposentar + cadastro["idade"]

for k, v in cadastro.items():
    print(f"{k} tem o valor {v}")
