numero = int(input("Quantos termos voce quer mostrar?"))
termo1 = 0
termo2 = 1
print ("{} - {}".format(termo1, termo2),end= "")
contador = 3
while contador <= numero:
    termo3 = termo1 + termo2
    print ("- {}".format(termo3), end = "")
    termo1 = termo2 
    termo2 = termo3
    contador = contador + 1
print (" fim ")