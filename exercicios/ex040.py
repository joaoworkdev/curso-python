nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2) /2
if media < 5.0:
    print ("O aluno ficou com a media {:.1f}, e está de REPROVADO!".format(media))
elif media <= 6.9:
    print ("O aluno ficou com a media {:.1f}, e está de RECUPERAÇÃO!".format(media))
else:
    print ("O aluno ficou com a media {:.1f}, e está APROVADO!".format(media))