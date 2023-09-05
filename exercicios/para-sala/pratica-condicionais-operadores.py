# Vamos pensar num exemplo. Imagine que você é um professor 
# e deve calcular a média das notas dos alunos em três provas. 
# Para facilitar, você quer escrever um código que calcule as 
# notas pra ti. Vamos criar uma função para isso e nós só 
# precisamos chamar essa função com as notas dos alunos! 

# definindo a função
def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

# definindo variáveis
nota1 = 9.4
nota2 = 9
nota3 = 10

# chamando a função
media_aluno = round(calcular_media(n1=nota1, n2=nota2, n3=nota3), 1)
print(media_aluno)


# Como saber se o aluno foi ou não aprovado?

# precisamos definir a média de aprovação e de recuperação

media_aprovacao = 7
media_recuperacao = 3
presenca = 90

# como saber se a nota do aluno é maior que a média de aprovação?

# verificar se a média do aluno é maior ou igual a media da aprovação
if (media_aluno >= media_aprovacao) and presenca > 75:
    if media_aluno >= 9.5:
        print("Aprovado com mérito")
    else:
        print("Aprovada")
# se não for, verificar se é igual ou maior a médio de recuperação
elif (media_aluno >= media_recuperacao) or presenca > 50:
    print("Recuperação")
# se não for
else:
    print("Reprovado")

print("Fim do programa")