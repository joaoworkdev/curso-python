numero = int(input("Digite um numero:"))
print ("[ 1 ] BINARIO")
print ("[ 2 ] OCTAL")
print ("[ 3 ] HEXADECIMAL")
escolha = int(input("Sua escolha:"))
if escolha == "1":
    print("{} convertido para binario é {}".format (numero,bin(numero))) 
elif escolha == "2":
    print ("{} convertido para Octal é {}".format(numero, oct(numero)))
else:
    print ("{} convertido para hexadecimal é {}".format(numero, hex(numero)))
    