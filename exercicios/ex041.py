from datetime import date
atual = date.today().year
nascimento = int(input("Digite o ano de nascimento:"))
idade = atual - nascimento
print ("O atleta tem: {} anos.".format(idade))
if idade <= 9:
    print ("MIRIM")
elif idade <= 14:
    print ("INFANTIL")
elif idade > 14 and idade <= 19:
    print ("JUNIOR")
elif idade <= 25:
    print ("SENIOR")
else:
    print ("MASTER")
