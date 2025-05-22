lanche = ("Hamburguer","Suco","Pizza","Pudim")
for contador in range(0,len(lanche)):
    print(f"Eu vou comer na posição {contador} {lanche[contador]}")
for comida in lanche:
    print (f"Eu vou comer {comida}")
print ("Comi muito")
for pos, comida in enumerate(lanche):
    print (f"Eu vou comer {comida} na posição {pos}")
print (lanche[2])
print (lanche[0])
print (lanche[1:3])
print (lanche[-3])
print (lanche[0:])
print (lanche[:2])
print ("FIM!")
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print (sorted(a))
print (c) 