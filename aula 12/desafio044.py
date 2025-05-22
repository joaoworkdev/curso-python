valor = float(input("Valor do produto:"))
pagamento = str(input("Forma de pagamento:"))
if pagamento == "dinheiro" or "cheque":
    novovalor = valor - (valor * 10 /100)
    print ("O valor do produto com desconto de 10% é {}".format(novovalor))
elif pagamento == "cartao":
    novovalor = valor - (valor * 5 /100)
    print("O valor do produto com desconto de 5% é: {}".format(novovalor))
elif pagamento == "dividir":
    print ("O valor divido em até 2x, será {}".format(valor))
elif pagamento == "dividir3":
    novovalor = valor + (valor * 20 / 100)
    print ("O valor total com juros, será {}".format(novovalor))