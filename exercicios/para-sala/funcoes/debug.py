#print("Marcinha")

def calcular_media(n1, n2): #python define para mim uma funçao calcular_media (n1,n2) :=>contentação
    media_total = (n1 + n2)/2   #o q vc quiser fazer somar/multiplicar ou seila o que.
    return media_total
 
nota1 = 7
nota2 = 6
    
media_aluna = calcular_media(nota1, nota2)
print(media_aluna)

media_aprovacao = 5
media_recuperacao = 3
 
if media_aluna >= media_aprovacao:  #não esquecer o :(dois pontos) 
    print("Aprovada Maravilhosa")
elif media_aluna >= media_recuperacao:
    print("Recuperação ;/")
else:
    print("Reprovada,:/")
print("Fim do programa")








   