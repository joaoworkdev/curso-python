frase = str(input("Digite uma frase:")).upper().strip()
print (frase.count("a"))
print ("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print ("A ultima letra A aparece na posição {}".format(frase.rfind("A")+1))