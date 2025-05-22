numero = 0
soma = 0
digitados = 0
while numero != 999:
    numero = int(input("Digite um valor:"))
    if numero == 999:
        break
    digitados = digitados + 1
    soma = soma + numero
print(f"foram digitados {digitados} numeros e a soma dos valores é {soma}")