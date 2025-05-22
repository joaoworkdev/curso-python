# funções
def mostrarLinha():
    print("-" * 30)

mostrarLinha()
print("       SISTEMA DE ALUNOS     ")
mostrarLinha()
print("      CADASTRO DE FUNCIONARIOS     ")
mostrarLinha()
print("        ERRO DO SISTEMA      ")
mostrarLinha()

# Parametros

def mensagem(msg):
    print("=" * 30)
    print(msg)
    print("=" * 30)

mensagem("Sistema de Alunos")
mensagem("Curso em video")

# Pratica

def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")

soma(4, 5)
soma(8, 9)
soma(2, 1)  

# Parametros empacotados

def contador(*num):
    for valor in num:
        print(f"{valor} ", end="")
    print("Fim!") 

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Tamanho 

def contador(*num):
    tamanho = len(num)
    print(f"Recebi os valores {num} e são ao todo {tamanho} numeros")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# funções com listas
def dobra(lista):
    pos = 0
    while pos < len(lista):
         lista[pos] *= 2
         pos += 1
    print(valores)

valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
