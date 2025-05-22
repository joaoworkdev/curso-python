num1 = int(input("Digite um valor:"))
num2 = int (input("Digite outro valor:"))
resp = "0"
maior = num1
while resp != "0":
    resp = str(input(""""
                    [1] SOMAR
                    [2] MULTIPLICAR
                    [3] MAIOR
                    [4] NOVOS NUMEROS
                    [5] SAIR DO PROGRAMA
                     """))
    if resp == "5":
        print ("Voce saiu do programa")
    elif resp == "1":
        soma = num1 + num2
        print ("A SOMA DOS NUMEROS {} + {} = {}".format(num1, num2, soma))
    elif resp == "2":
        multi = num1 * num2
        print ("A MULTIPLICAÇÃO DOS NUMEROS {} * {} = {}".format(num1, num2, multi))
    elif resp == "3":
        if maior < num2:
            maior = num2
            print("O MAIOR NUMERO DIGITADO FOI {}".format(maior))
        else:
            print ("O maior numero digitado foi {}".format(maior))
    elif resp == "4":
        num1 = int(input("Digite um novo valor:"))
        num2 = int(input("Digite outro valor:"))
print ("O programa foi encerrado!")
