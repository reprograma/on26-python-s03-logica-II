# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
              #Até 5 Kg               Acima de 5 Kg
#Morango      R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã         R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
# quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# informar o peso a ser comprado

peso_morango = float(input("Quantos Kg de morango deseja comprar?\n"))
preco_ate_5kg_morango = 2.5
preco_acima_5kg_morango = 2.2

peso_maca = float(input("Quantos Kg de maça deseja comprar?\n"))
preco_ate_5kg_maca = 1.8
preco_acima_5kg_maca = 1.5

# calcular o preço de acordo com o peso a ser comprado

if peso_morango <= 5:
    preco_morango = round((peso_morango * preco_ate_5kg_morango), 1)
elif (peso_morango > 5):
    preco_morango = round((peso_morango * preco_acima_5kg_morango), 1)
print("\nVocê irá pagar " + str(preco_morango) + " reais por " + str(peso_morango) + " Kg de morango.")

if peso_maca <= 5:
    preco_maca = round((peso_maca * preco_ate_5kg_maca), 1)
elif peso_maca > 5:
    preco_maca = round((peso_maca * preco_acima_5kg_maca), 1)
print("\nVocê irá pagar " + str(preco_maca) + " reais por " + str(peso_maca) + " Kg de maçã.")

# calcular o valor total da compra e se é passível de desconto

preco_total = preco_morango + preco_maca
peso_total = peso_morango + peso_maca

peso_para_desconto = 8
preco_para_desconto = 25
desconto = 0.90

if peso_total > peso_para_desconto or preco_total > preco_para_desconto:
    preco_com_desconto = round((preco_total * desconto), 1)
    print("\nO preço total da sua compra com desconto será de " +str(preco_com_desconto) + " reais.\n")
else:
    print("\nO preço total da sua compra será de " + str(preco_total) + " reais.\n")