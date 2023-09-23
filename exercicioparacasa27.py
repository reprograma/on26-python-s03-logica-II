def calcular_valor_compra(kg_morangos, kg_macas):
    preco_morango = 2.5 if kg_morangos <= 5 else 2.2
    preco_maca = 1.8 if kg_macas <= 5 else 1.5
    
    valor_total = (preco_morango * kg_morangos) + (preco_maca * kg_macas)
    
    if (kg_morangos + kg_macas) > 8 or valor_total > 25:
        desconto = valor_total * 0.1
        valor_total -= desconto
    
    return valor_total

kg_morangos = float(input('quantidade de morangos (em Kg): '))
kg_macas = float(input('quantidade de maçãs (em Kg): '))

valor_a_pagar = calcular_valor_compra(kg_morangos, kg_macas)
print(f'valor a ser pago: R$ {valor_a_pagar:.2f}')

# teste
