def calculo_media(nota1, nota2, nota3):
    media =  (nota1 + nota2 + nota3)/3 
    print(media)

nota1, nota2, nota3 = 10, 8, 7 
calculo_media(nota1, nota2, nota3)

#################

def calculo_media(nota1, nota2, nota3):
    media =  (nota1 + nota2 + nota3)/3 
    print('Nota1: ' + str(nota1))
    print('Nota2: ' + str(nota2))
    print(media)

nota1 = 10
nota2 = 8
nota3 = 7 
calculo_media(nota2=nota1, nota1=nota2, nota3=nota3)
print('Nota1 ' + str(nota1))

#########################

def calculo_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    media =  (nota1 * peso1 + nota2 *peso2 + nota3 * peso3)/(peso1 + peso2 + peso3)
    print(media)

nota1, nota2, nota3 = 10, 10, 1
peso1, peso2, peso3 = 1, 3.5, 5.5
calculo_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3)

########################

def calculo_recuperação(nota_regular, nota_recuperação):
    media_final = (nota_regular + nota_recuperação)/2
    print(media_final)


def calculo_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    media =  (nota1 * peso1 + nota2 *peso2 + nota3 * peso3)/(peso1 + peso2 + peso3)
    return media

nota1, nota2, nota3 = 10, 10, 1
peso1, peso2, peso3 = 1, 3.5, 5.5
nota_recuperação = 7
media_regular = calculo_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3)
calculo_recuperação = calculo_recuperação(media_regular, nota_recuperação)

###############################


media = lambda nota1, nota2 : (nota1 + nota2)/2
print(media(1,3))


#######################

import math 

print(math.pi)

#####################

from random import randrange, choice

print(choice(['a', 'b', 'c']))

########input

entrada = input("Informe um numero: ")

###########

entrada1 = input("Informe o primeiro valor: ")
entrada2 = input("Informe o segundo valor: ")

print(type(entrada1))
print(type(entrada2))

concat = entrada1 + entrada2
print("Concat: " + concat)

print("Tipo da variável concat: " + str((type(concat))))

