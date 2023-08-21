#operador condicional = if, else, elif
#operadores relacionais = <,>, ==, !=, <=, >=.
def calcular_media(n1, n2):
    media = (n1+n2 )/2
    return media

nota1 = float(input("digite a nota 1:"))
nota2 = float(input("digite a nota 2: "))
media_da_aluna = calcular_media(nota1, nota2)

print(f"A média do aluna é : {media_da_aluna:.2f}")

media_aprovada = 5
media_de_recuperacao = 3

if media_da_aluna  >= media_aprovada:
    print('Aprovada, uhuul parabéns!')
elif media_da_aluna >= media_de_recuperacao:
    print("Bora se esforçar que tu está de recuperação, mas eu acredito em você!")
else:
    print('Não foi dessa vez, se esforçe mais!')

#Or e and

presenca = 99

if (media_da_aluna >= media_aprovada) and presenca > 70:
    if media_da_aluna > 9.5:
        print("Arrasou, aprovada com mérito!")
elif (media_da_aluna >= media_aprovada) or presenca >= 50:
    print('Aprovada')
else:
    print("reprovada")

