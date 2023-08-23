#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

quantidade_morangos = float(input("Quantidade de morangos (em Kg): "))
quantidade_macas = float(input("Quantidade de maçãs (em Kg): "))

valor_morangos = quantidade_morangos * 2.5
if quantidade_morangos >= 5:
    valor_morangos = quantidade_morangos * 2.2

valor_macas = quantidade_macas * 1.8
if quantidade_macas >= 5:
    valor_macas = quantidade_macas * 1.5

valor_total = valor_morangos + valor_macas

if quantidade_morangos + quantidade_macas > 8 or valor_total >= 25 :
    valor_com_desconto = valor_total * 0.1
    valor_total = valor_total - valor_com_desconto

print(f"O valor total é R$ {valor_total:.2f}")

