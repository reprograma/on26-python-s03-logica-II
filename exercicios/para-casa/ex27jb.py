# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas 
# e escreva o valor a ser pago pelo cliente.
#   Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda
# um desconto de 10% sobre este total. 


preco_morango_menor_5kg = 2.50
preco_morango_maior_5kg = 2.20

preco_maca_menor_5kg = 1.80
preco_maca_maior_5kg = 1.50

qtd_morango = 6
qtd_maca = 4
total_frutas = 10

if qtd_morango < 5:
    valor_morango = qtd_morango * preco_morango_menor_5kg
else:
    valor_morango = qtd_morango * preco_morango_maior_5kg
print(valor_morango)    

if qtd_maca < 5:
    valor_maca = qtd_maca * preco_maca_menor_5kg
else:
    valor_maca = qtd_maca * preco_maca_maior_5kg
print(valor_maca)

if total_frutas > 8:
    valor_total = (valor_morango + valor_maca)
print(valor_total)

valor_compra = valor_total - (valor_total * 0.1)
print(valor_compra)
    
