casa = float(input("Qual valor da casa?"))
salario = float(input("Qual salario?"))
anos = int(input("Quantos anos de financiamento?"))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print ("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}".format(casa,anos, prestacao))
if prestacao <= minimo:
    print ("Recusado")
elif prestacao > minimo:
    print ("Aprovado")