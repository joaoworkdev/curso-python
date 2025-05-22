from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),randint(1, 10))
print ("Os valores sorteados foram: ", end="")
for contador in numero:
    print (f"{contador} ", end="")
print (f"\nO maior valor sorteado foi: {max(numero)}")
print (f"O menor valor sorteado foi: {min(numero)}")