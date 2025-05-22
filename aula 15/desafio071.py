saque = int(input("Qual valor do saque?"))
total = saque
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total = total - cedula
        totalcedula = totalcedula + 1
    else:
        if totalcedula > 0:
            print (f"Total de {totalcedula} cedulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print ("Volte sempre!")