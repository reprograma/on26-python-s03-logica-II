#27-Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
#  (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor 
# a ser pago pelo cliente.




morango_peso = float(input("Digite kg de morango: "))
maca_peso = float(input("Digite kg de maça: "))


if morango_peso > 5:
   preco_morango = 2.20
else:
   preco_morango = 2.50

if maca_peso > 5:
   preco_maca = 1.50
else:
   preco_maca = 1.80


#calculo das frutas

valor_total_frutas =  ( morango_peso * preco_morango ) + (maca_peso * preco_maca)


if (morango_peso + maca_peso ) > 8 or calculo_total_fruta > 25:
    valor_total_frutas = valor_total_frutas * 0.9
    

print(f"Seu valor total é {valor_total_frutas:,.2f} : ")
    

#feito em grupo <3