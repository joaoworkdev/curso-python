salario = float(input("Digite o valor do salario do funcionario:"))
if salario <= 1250.00:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)
print ("O salario é {} e agora o total a ganhar sera de {}".format(salario, aumento))
