def calcular_media(n1, n2):
    media_dentro_da_funcao = (n1 + n2)/2
    return media_dentro_da_funcao


nota1 = 10
nota2 = 4
media_do_aluna = calcular_media(nota1, nota2)

print(media_do_aluna)

media_de_aprovacao = 5
media_de_recuoeracao = 3
presenca = 99
                                     #AND ou OR
if (media_do_aluna >= media_de_aprovacao) or presenca > 70:
    if media_do_aluna > 9.5:
        print("Super ")


if type(media_do_aluna) == float:
    print("Qualificadíssima para ")
if media_do_aluna >= media_de_aprovacao:
    print("Qualificada para ")
elif media_do_aluna >= media_de_recuoeracao:
    print("Recuperação")
else:
    print("Desqualificada para ")

numero1 = 0.0
string1 = ""

if numero1:
    print("Numero não é zero")
else:
    print("Numero é zero")
    
print("Garota de programa")






if numero_de_kg_de_maca > 5:
    preco_das_macas = numero_de_kg_de_maca * pre