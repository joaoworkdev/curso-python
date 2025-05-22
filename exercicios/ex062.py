primeiro = int(input("PRIMEIRO TERMO?"))
razao = int(input("Razao da PA?"))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(" {} ".format(termo), end="")
        termo = termo + razao
        contador = contador + 1
    print (" PAUSA ")
    mais = int(input("Quantos termos voce quer mostrar a mais?"))
print ("Progressão finalizada com {} termos mostrados".format(total))