numero = int(input("Digite um numero:"))
total = 0
for contador in range(1,numero+1):
    if numero % contador == 0:
        print("\033[33m", end=" ")
        total = total + 1
    else:
        print ("\033[31m", end=" ")
    print ("{}".format(contador), end=" ")
print ("numero {} foi divisivel {} vezes".format(numero, total))
if total == 2:
    print ("Ele é primo")
else:
    print ("Ele não é primo")
    