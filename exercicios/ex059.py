numero1 = int(input("Digite o primeiro valor:"))
numero2 = int(input("Digite o segundo valor>"))
resposta = 0
while resposta != 5:
    print (""" 
           [1] soma
           [2] multiplicar
           [3] maior
           [4] novos numeros
           [5] sair do programa""")
    resposta = int(input("Qual é a opção?"))
    if resposta == 1:
        soma = numero1 + numero2
        print ("A soma entre {} + {} = {}".fomrat(numero1, numero2, soma))
    elif resposta == 2:
        multi = numero1 * numero2
        print("A multiplicação entre {} * {} = {}".format(numero1,numero2, multi))
    elif resposta == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print ("Entre {} e {} o maior numero é {}".format(numero1,numero2, maior))
    elif resposta == 4:
        numero1 = int(input("Digite um novo valor:"))
        numero2 = int(input("Digite o outro valor:"))
    elif resposta == 5:
        print ("Voce encerrou o programa!")
    else:
        print ("RESPOSTA INVALIDA")
print("Fim do programa!")

