#terceira semana

*Argumentos = valor dos parâmentros;*

*constante é uma variavel que não muda de valor*

*boas práticas em uma função, sempre colocar as variaveis depois de chamar a função*

import math

numero1 = 25
print(math.sqrt(numero1))#sqrt é a raiz quadradada


#### caso não queira importar algo especifico dentro da biblioteca

from math import sqrt

numero1 = 25
print(sqrt(numero1))

####

print(math.log(10, 2))

###

print(math.sin(10))#seno

print(math.cos(2))#cosseno

#para printar com o pi

print(math.pi)

#para potencia

print(math.pow(2,3))

#usar round

valor_de_pi = math.pi
print(round(valor_de_pi,2)) 

#sempre passe o numer de casas que você quer que ele retorne;
#caso não coloque a casa decimais o round ele arredonda

#função lambda é usada em data  science 

# Debugging

com ele conseguimes ver linha por linha apra entender o  que está acontecendo, para poder entender e arrumar. 

import math

#usar round

valor_de_pi = math.pi
print(round(valor_de_pi,2)) 
#sempre passe o numer de casas que você quer que ele retorne;
#caso não coloque a casa decimais o round ele arredonda

play - (f5) - ele vai executar até o outro breakpoint;

Step over (f10) - é para rodar somente uma linha;

#debugg

print("stefany")


#exercicios de notas
#em "def calcular_media(n1, n2):" eu defino os parametros da função
def calcular_media(n1, n2):
    media = (n1+n2 )/2
    return media

nota1 = float(input("digite a nota 1:"))
nota2 = float(input("digite a nota 2: "))


print(f"A média do aluno é : {calcular_media(nota1, nota2):.2f}")

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

#no python quando:
num = 0
str =""

ele considera como falso

