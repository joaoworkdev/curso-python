def area(largura, comprimento):
    a = largura * comprimento
    print(f"A area de um terreno {largura} x {comprimento} é de {a}m ")

print(" Controle de Terrenos ")
print("-" * 20)
l = float(input("Largura: "))
c = float(input("Comprimento: "))
area(l, c)