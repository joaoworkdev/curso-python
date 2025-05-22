primeirotermo= int(input("Digite uma PA:"))
razao = int(input("Digite a razão:"))
termo = primeirotermo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= 10:
        print ("{}".format(termo),end="")
        termo = termo + razao
        contador = contador + 1
        print ("PAUSA")
        mais = int(input("Quantos termos voce quer mostrar a mais?"))
print ("fim")