lanche = ["Hamburguer", "Suco", "Pundim", "Pudim"]
print (lanche)
lanche[3] = "Picole"
print (lanche)
lanche.append("Cokie")
print(lanche)
lanche.insert(1,"Cachorro quente")
print(lanche)
del lanche[3]
print (lanche)
lanche.pop(2)
print (lanche)
if "Cokie" in lanche:
    lanche.remove("Cokie")
print (lanche)

valores = list(range(4,11))
valores.sort()
print (valores)
valores.sort(reverse=True)
print(valores)
print(len(valores))

numeros = list()
for cont in range(0,5):
    numeros.append(int(input("Digite um valor:")))
for contador, n in enumerate(numeros):
    print(f"Na posição {contador} encontrei o valor {n}")
print ("Cheguei ao final da lista")