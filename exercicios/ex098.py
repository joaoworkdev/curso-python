from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    print("-" * 20)
    print(f"Contagem de {i} até o {f} de {p} em {p  }")
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i 
        while cont >= f:
            print(f"{cont} ",end="", flush=True)
            sleep(0.5)
            cont -= p
        print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
print("=" * 20)
print("Agora é sua vez...")
inicio = int(input("Inicio: "))
fim = int(input("Fim:   "))
passo = int(input("Passo:   "))
contador(inicio, fim, passo)
