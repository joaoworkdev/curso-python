nomebarato = " "
resp = "S"
valortotal = acima1000 = menor = valor = contador = 0
while True:
    nome = str(input("Nome do produto:"))
    valor = float(input("Digite o valor do produto:"))
    contador = contador + 1
    valortotal = valortotal + valor
    if valor > 1000:
       acima1000 = acima1000 + 1
    if contador == 1:
       menor = valor
    else:
       if valor < menor:
          menor = valor
          nomebarato = nome
    resp = str(input("Voce quer continuar [S/N]?")).upper().strip()[0]
    if resp == "N":
       break
print (f"O valor total da compra é {valortotal}")
print (f"Ao total tem {acima1000} produtos custando acima de R$1000,00")
print (f"O produto mais barato é {nomebarato}, custando R${menor}")