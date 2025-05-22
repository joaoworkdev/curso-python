preco = float(input("Digite o valor do produto:"))
desconto = preco - (preco * 10/100)
parcelado = preco + (preco * 8/100)
print ("O preço do produto é R$ {} se o pagamento for a vista ele sair por R$ {} mas se for parcelar acrescenta um juros de 8%. e sair no valor de R$ {}".format(preco,desconto,parcelado))