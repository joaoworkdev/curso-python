nota1 = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a segunda nota do aluno:"))
media = (nota1 + nota2)/2
if media < 5.0: 
    print ("REPROVADO! sua média foi: {:.1f}".format(media))
elif media <= 6.9:
    print ("RECUPERAÇÃO! sua media foi: {:.1f}".format(media))
else:
    print ("APROVADO! Sua media foi: {:.1f}".format(media))
