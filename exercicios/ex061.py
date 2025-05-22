primeirotermo= int(input("Digite uma PA:"))
razao = int(input("Digite a razão:"))
termo = primeirotermo
contador = 1
while contador <= 10:
    print ("{} ".format(termo), end="")
    termo = termo + razao
    contador = contador + 1
print ("FIM")
