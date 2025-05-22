def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return(f"Com {idade} anos: Não vota!")
    elif idade < 18 and idade >= 16 or idade > 65:
        return(f"Com {idade} anos: Voto opcional!")
    else:
        return(f"Com {idade} anos: Voto Obrigatorio!")
    

print(voto(2000))

