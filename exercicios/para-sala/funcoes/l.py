def calcular_media(n1, n2):
    media_aluno = (n1 + n2)/2
    return media_aluno

nota1 = 10
nota2 = 9

media_aluno = calcular_media(nota1, nota2)
print(media_aluno)

media_de_aprovacao = 5
media_de_recuperacao = 3

if type(media_aluno) == float:
    media_aluno = round(media_aluno)

if media_aluno >= media_de_aprovacao:
    if media_aluno > 9.5:
        print("Aprovado com mérito")
    else:
        print("Aprovado")
elif media_aluno >= media_de_recuperacao:
    print("Recuperação")
elif media_aluno >= 1:
    print("Desclassificada")
else:
    print("Reprovado")

print("Fim do programa")

