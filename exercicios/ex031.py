distancia = float(input("Qual a distancia da viagem?"))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print ("O valor da sua viagem com a distancia de {} é {}".format(distancia,valor))