reta1 = float(input("Primeiro segmento:"))
reta2 = float(input("Segundo segmento:"))
reta3 = float(input("Terceiro segmento:"))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3  and reta3 < reta1 + reta2:
    print ("Os segmentos formam um triangulo!")
else: 
    print ("Os segmentos nao formam um triangulo")