#Condiçoes aninhadas
nome = str(input("Qual o seu nome?"))
if nome == "Gustavo":
    print("Que nome bonito!")
elif nome == "Pedro" or "Maria":
    print("Seu nome é popular no brasil")
elif nome in "Ana Claudia Jessica Juliana":
    print ("Belo nome feminino")
else:
    print ("Seu nome é bem normal!")
print ("Tenha um bom dia {}".format(nome))