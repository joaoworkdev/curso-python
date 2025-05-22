#fatiamento de string
frase = "Curso em video python"
print (frase [9])
print (frase [9:13])
print (frase[9:21])
print (frase[9:21:2])
print (frase[:5])
print (frase[15:])
print (frase[9::3])
#Analise de string
print(len (frase))
print(frase.count ("o"))
frase.count ("o",0,13)
print(frase.find ("deo"))
print(frase.find ("Android"))
print("Curso" in frase)
#Transformação
print(frase.replace("pyhon","Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
#divisao
print(frase.split())
dividido = frase.split()
print(dividido[2])
#junção
print("-".join(frase))
frase2 = "   Aprenda Python  "   
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

