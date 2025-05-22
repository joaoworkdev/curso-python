import datetime
data_atual = datetime.datetime.now().year
maioridade = 0
menoridade = 0
for contador in range(1,7+1):
    ano = int(input("Digite o ano de nascimento:"))
    if data_atual - ano >= 18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print ("Existem {} pessoas maiores de idade, e {} pessoas de menor idade".format (maioridade, menoridade))