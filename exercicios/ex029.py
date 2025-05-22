velocidade = float(input("Qual a velocidade do carro?"))
if velocidade > 80:
    print ("MULTADO! Você excedeu o limite permitido que é de 80km/h")
    valor = (velocidade - 80) * 7
    print ("O valor da multa de acordo com sua velocidade é {}".format(valor))
print ("Tenha um bom dia! Dirija com segurança!")