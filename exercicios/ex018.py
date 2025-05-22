import math
angulo = float(input("Digite o angulo:"))
seno = math.sin(math.radians(angulo))
print ("O angulo {} é o SENO {:.2f}".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print ("O angulo {} é o COSSENO {:.2f}".format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print ("O angulo {} é o TANGENTE {:.2f}".format(angulo,tangente))
