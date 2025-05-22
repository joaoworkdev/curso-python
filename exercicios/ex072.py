decimal = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input("Digite um valor:"))
    if numero >= 0 and numero <= 20:
        print (f"Voce digitou o numero {decimal[numero]}")
        resp = str(input("Voce quer continuar? [S/N]")).upper().strip()[0]
        if resp == "S":
            print ("cotinuando...")
        else: 
            break
    else:
        print ("Tente novamente")
print ("ENCERRADO")