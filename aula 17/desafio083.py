expressao = str(input("Digite a expressão:"))
pilha = list()
for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão está válida")
else:
    print("Sua expressão está incorreta")
