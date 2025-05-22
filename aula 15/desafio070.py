resp = "S"
soma = 0
valoralto = 0
barato = float("inf")
nome = ""
nomebarato = ""
while resp == "S":
    nome = str(input("Digite o nome do produto:"))
    preco = float(input("Digite o valor do produto:"))
    if preco < barato:
        barato = preco
        nomebarato = nome
    if preco > 1000:
        valoralto = valoralto + 1
    resp = str(input("Voce quer continuar [S/N]")).upper().strip()[0]
    soma = soma + preco
print (f"O valor da compra é R${soma}")
print (f"Ao total tem {valoralto} produtos com valor acima de R$ 1000,00")
print (f"O produto mais barato é {nomebarato} e custa {barato}")
