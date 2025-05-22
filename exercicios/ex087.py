matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapar = somacoluna = maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor na {[linha],[coluna]} posição"))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end= "")
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()

for linha in range(0,3):
    somacoluna += matriz[linha][2]

for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif  matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
        
print(f"A soma dos pares é {somapar}")
print(f"A soma da terceira coluna é {somacoluna}")
print(f"O maior valor é {maior}")
