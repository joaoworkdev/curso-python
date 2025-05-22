from datetime import date
atual = date.today().year
maior = 0
menor = 0
for contador in range (1,7+1):
    nascimento = int(input("Ano de nascimento:"))
    idade = atual - nascimento
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print ("Total de maiores de idade é {}".format(maior))
print ("Total de menor de idade é {}".format(menor))
    