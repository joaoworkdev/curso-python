numero = 0
soma = 0
digitados = 0
while True:
    numero = int(input("Digite um numero:"))
    if numero == 999:
        break
    soma = numero + soma
    digitados = digitados + 1
print (f"a soma dos valores é {soma}")
print (f"Foram digitados {digitados} numeros")