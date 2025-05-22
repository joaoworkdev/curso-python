from random import randint 
numero = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print ("Os numeros sorteados foram: ", end= "")
for contador in numero:
    print (f"{contador} ", end= "")
print(f"\nO maior valor sorteado foi: {max(numero)}")
print (f"O menor valor sorteado foi: {min(numero)}")
