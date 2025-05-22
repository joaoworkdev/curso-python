contador = int
for contador in range(1,10):
    print (contador)
#aula pratica
for contador in range(0, 6):
    print ("Oi")
print ("FIM")
#Outro exemplo
for contador in range(6,0, -1):
    print (contador)
#outro exemplo
num = int(input("Digite um numero:"))
for contador in range(0, num+1):
    print (contador)
#outro exemplo[
inicio = int(input("Digite um numero para iniciar contagem:"))
fim = int(input("Digite o numero para parar de contar:"))
pular = int(input("Digite quanto voce quer pular:"))
for contador in range(inicio, fim+1, pular):
    print(contador)
print ("FIM")
#outro exemplo
soma = 0
for contador in range (0, 4):
    num = int(input("Digite um numero para somar:"))
    soma = soma + num 
print ("A soma de todos os numeros é: {}".format(soma))