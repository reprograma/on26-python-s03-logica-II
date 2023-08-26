#exercicico 27

#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


#passo a passo:
#descobrir os valores das maças e morangos com a regra >= 5kg
#descobrir o total do valor da compra ou o peso para colocar a regra de desconto

#parte 1
#variaves
morango_por_kg_ate_5kg = 2.5
maca_por_kg_ate_5kg = 1.8
maca_por_kg_maior_5kg = 1.5
morango_por_kg_maior_5kg = 2.2

maca_kg = float(input("Quantos kilos de maças? "))
morango_kg = float(input("Quantos kilos de morangos? "))

total_frutas_kg = maca_kg + morango_kg

valor_maca = 0
valor_morango = 0

#parte 2
#calcula o valor das maçãs
if maca_kg <= 5:
    valor_maca = maca_kg * maca_por_kg_ate_5kg
else:
    valor_maca = maca_kg * maca_por_kg_maior_5kg

#calcula o valor dos morangos
if morango_kg <= 5:
    valor_morango = morango_kg * morango_por_kg_ate_5kg
else:
    valor_morango = morango_kg * morango_por_kg_maior_5kg

#calcula o valor total
valor_total = valor_maca + valor_morango

#Aplica desconto, se necessário
if total_frutas_kg > 8 or valor_total > 25:
    valor_total = valor_total * 0.9

print(f"Valor a ser pago: R$ {valor_total:.2f}")