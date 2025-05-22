frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range (len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print ("O inverso de {} e {}".format(junto,inverso))
if inverso == junto:
    print ("TEMOS UM PALINDROMO")
else:
    print ("Nao temos um palindromo")