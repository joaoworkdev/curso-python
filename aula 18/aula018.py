teste = list()
teste.append("Gustaavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

# OUTRO EXEMPLO

galera = [["João", 19],["Ana", 33],["Joaquim", 13],["Maria", 45]]
print(galera)
print(galera[0])
print(galera[0][1])

for cadapessoa in galera:
    print(f"nomes: {cadapessoa[0]} tem {cadapessoa[1]
    } anos de idade")

turma = list()
dados = list()
for contador in range(0,3):
    dados.append(str(input("Digite seu nome:")))
    dados.append(int(input("Digite sua idade:")))
    turma.append(dados[:])
    dados.clear()

print(turma) 