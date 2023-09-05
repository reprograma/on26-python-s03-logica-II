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
nota1 = 8
nota2 = 4
nota3 = 7

# chamando a função
media_final = round(calcular_media(n1=nota1, n2=nota2, n3=nota3), 1)
print(media_final)



