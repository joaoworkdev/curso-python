reta1 = float(input("Tamanho da reta?"))
reta2 = float(input("Tamanho da reta?"))
reta3 = float(input("Tamanho da reta?"))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print ("Os segmentos acima podem formar um triangulo")
    if  reta1 == reta2 and reta2 == reta3:
        print ("EQUILATERO!")
    elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print ("ESCALENO!")
    else: 
        print ("ISOCELES")
else:
    print ("Não da pra formar triangulo com as retas")