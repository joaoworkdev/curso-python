from datetime import date
anoatual = date.today().year
nascimento = int(input("Digite o ano que nasceu:"))
sexo = str (input("Qual seu sexo: [F/M]"))
idade = anoatual - nascimento
print ("Quem nasceu em {}, tem {} anos em {}".format(nascimento,idade,anoatual)) 
if sexo == "m":
    if idade < 18:
        tempo = 18 - idade
        print ("Falta {} anos, para voce se alistar".format(tempo))
        ano = anoatual + tempo
        print ("Seu alistamento será em {}.".format(ano))
    elif idade > 18:
        tempo = idade - 18
        print ("Já passou {} anos , para o prazo de se alistar".format(tempo))
        ano = anoatual - tempo
        print ("Seu alistamento foi em {}.".format(ano))
    else:
        print ("Vá se alistar imediatamente!")
else:
    print ("Você não e obrigada a se alistar!")
