c = ("\033[m",        # 0 sem cores
     "\033[0;30;41m", # 1 vermelho
     "\033[0;30;42m", # 2 verde
     "\033[0;30;43m", # 3 amarelo
     "\033[0;30;44m", # 4 azul
     "\033[0;30;45m", # 5 roxo
     "\033[0;30;46m", # 6 branco
    );

def ajuda(com):
    titulo(f"ACESSANDO O MANUAL DO COMANDO \'{com}\'", 4)
    print(c[6],end="")
    help(com)
    print(c[0], end="")

def titulo(msg, cor=0):   
    tam = len(msg) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end="")
    

comando = ""
while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    comando = str(input("Função ou bibloteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
print("ATE LOGO", 1)
