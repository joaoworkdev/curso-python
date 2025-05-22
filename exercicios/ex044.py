print("{:=^40}".format(" LOJAS DO JOÃO "))
preco = float(input("Preço das compras: R$"))
print ("""FORMAS DE PAGAMENTO
[1] à vista, dinheiro/cheque
[2] à vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão """)
resposta = int(input("Como voce quer pagar?"))
if resposta	== 1:
    valor = preco - (preco * 10 /100)
elif resposta == 2:
    valor = preco (preco * 5 /100)
elif resposta == 3:
    valor = preco
    parcela = valor / 2
    print ("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif resposta == 4:
    valor = preco + (preco * 20 /100)
    vezes = int(input("Quantas vezes vai parcelar?"))
    parcela = valor / vezes
    print ("Sua compra foi parcelas em {}x de R${:.2f}".format(vezes,parcela))
else:
    valor = 0
    print ("OPÇÃO INVALIDA DE PAGAMENTO!")
print("Sua compra de R${:.2f} vai custar R$ {:.2f}".format(preco, valor))