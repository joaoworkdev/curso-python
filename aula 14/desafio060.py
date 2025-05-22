contador = int(input("Digite um valor:"))
fatorial = 1
while contador > 1:
    fatorial = fatorial * contador
    contador = contador - 1
print (fatorial)
#outro exemplo
fatorial = 1
numero = int(input("Digite um valor:"))
for contador in range (numero,0, -1):
    fatorial = fatorial * contador
print (fatorial)