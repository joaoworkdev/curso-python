decimal = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input("Digite um numero:"))
    if numero >= 0 and numero <= 20:
        print (f"O numero digitado foi {decimal[numero]}")
        break
    else:
        print("Digite um valor entre 0 a 20")
print ("FIM")
