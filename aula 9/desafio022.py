nomecompleto = input("Qual seu nome completo?")
print(nomecompleto.upper())
print(nomecompleto.lower())
print(len(nomecompleto))
print(len(nomecompleto.replace(" ","")))
primeiro_nome = nomecompleto.split()[0]
contagem = len(primeiro_nome)
print(contagem)