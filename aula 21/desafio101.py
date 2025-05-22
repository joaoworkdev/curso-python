from datetime import datetime

def voto(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return("Voto negado")
    elif idade >= 16 and idade < 18:
        return("Voto opcional")
    else: 
        return("Voto Obrigatorio")
    
ano_nascimento = int(input("Digite o ano de nascimento:"))
resultado = voto(ano_nascimento)
print(resultado)