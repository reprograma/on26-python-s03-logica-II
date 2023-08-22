#questao27
# Uma fruteira esta vendendo frutas com a seguinte tabelas de preços:

# Até 5kg                     Acima de 5kg
#Morango R$ 2,50 por kg       R$2,20 por Kg
#Maçã R$ 1,80 por kg          R$1,50 por Kg


#Se o cliente comprar mais de 8Kg em frutas ou o valor ultrpassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg).

# Devera ser ultilizado int e input ou float
#int - se não houver partes fracionárias 
#float - permite qnt fracionarias 
#no caso em tela ultilizarei float (ex:caso seja 3.5kg)



qtd_morangos = float(input("Quantidade de morangos (em Kg): "))
qtd_macas = float(input("Quantidade de maçãs (em Kg): "))

# Cálculo do valor das frutas
valor_morangos = qtd_morangos * 2.50
if qtd_morangos > 5:
    valor_morangos = qtd_morangos * 2.20
    valor_macas = qtd_macas * 1.80
if qtd_macas > 5:
    valor_macas = qtd_macas * 1.50

    # Cálculo do valor total da compra
valor_total = valor_morangos + valor_macas
# Cálculo do desconto
if valor_total > 25 or qtd_morangos + qtd_macas > 8:
    desconto = valor_total * 0.10
    valor_total = valor_total - desconto
# Saída de dados
print("O valor a ser pago é de R$", valor_total)