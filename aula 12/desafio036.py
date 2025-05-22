valor = float(input("Qual o valor da casa?"))
salario = float(input("Qual salario do comprador?"))
anos = int(input("Quantos anos vai pagar?"))
valormensal =  valor / (anos * 12)
print ("O valor mensal da prestação da casa é {:.2f}".format(valormensal))
limite = salario * 0.30
if valormensal > limite:
    print ("O financiamento foi NEGADO")
elif valormensal <= limite:
    print ("O finacimento foi Aprovado!")

