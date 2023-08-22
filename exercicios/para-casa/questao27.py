## Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
## receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
## quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

import math

def calcular_valor_frutas(kg_morango, kg_maca):
    if kg_morango <= 5:
        preco_morango = 2.50
    else:
        preco_morango = 2.20

    if kg_maca <= 5:
        preco_maca = 1.80
    else:
        preco_maca = 1.50
    valor_total = (kg_morango * preco_morango) + (kg_maca + preco_maca)

    if (kg_morango + kg_maca) > 8 or valor_total > 25:
        desconto = valor_total * 0.1
        valor_total = desconto

    return valor_total                   

kg_morango = float(input("Digite a quantidade de morangos (kg): "))
kg_maca = float(input("Digite a quantidade de macas (kg): "))

valor_a_pagar = calcular_valor_frutas(kg_morango, kg_maca)
print(f"Valor: R$(valor_a_pagar: .2f)")

