# Interactive help
help(print)

help(input)


def contador(i,f,p):
    """
    DOCSTRINGS
    faz uma contagem e nostra na tela.
    i: inicio da contagem;
    f: fim da contagem;
    p: passo da contagem (pular)
    return: sem retorno 
    """
    cont = i
    while cont <= f:
        print(f"{cont} ", end= "")
        cont += p
    print("Fim")

contador(0, 100, 10)

help(contador)

# Parametros opcionais 
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale: {s} ")

soma(3, 2, 5)
soma(8, 4)  

# Escopo de variaveis 
def teste():
    x = 8 #ESCOPO LOCAL
    print(f"Na função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")

n = 2 #ESCOPO GLOBAL
print(f"No programa principal, n vale {2}")

#OUTRO EX:
def funcao():
    n1 = 4
    print(f"N1 local vale {n1} ")

n1 = 2
funcao()
print(f"N1 global vale {n1}")

#OUTRO EX:
def funcao():
    global n1
    n1 = 4
    print(f"N1 local vale {n1} ")

n1 = 2
funcao()
print(f"N1 global vale {n1}")

# Retorno de valores

def soma (a=0, b=0, c=0):
    s = a + b + c
    return s

resp = soma(3, 2, 5)
resp2 = soma(1, 7)
resp3 = soma(4)
print(f"As somas valem {resp}")
