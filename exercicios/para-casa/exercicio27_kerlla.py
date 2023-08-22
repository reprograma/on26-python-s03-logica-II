valor_total_compra = 0  # Defina o valor total da compra
quantidade_compra_morango = float(input("Digite a quantidade de morangos em Kg: "))  # Solicitar a quantidade de morango comprada
quantidade_compra_maca = float(input("Digite a quantidade de maçãs em Kg: "))  # Solicitar a quantidade de maçã comprada

# Cálculo do valor por kg de morango
if quantidade_compra_morango <= 5:
    valor_kg_morango = 2.50
else:
    valor_kg_morango = 2.20

# Cálculo do valor por kg de maçã
if quantidade_compra_maca <= 5:
    valor_kg_maca = 1.80
else:
    valor_kg_maca = 1.50

# Cálculo do valor total da compra
valor_total_compra = (quantidade_compra_morango * valor_kg_morango) + (quantidade_compra_maca * valor_kg_maca)

# Aplicar o desconto de 10% se a compra atender a condição
if (quantidade_compra_morango + quantidade_compra_maca) > 8 or valor_total_compra > 25.00:
    valor_total_compra *= 0.90  # Aplicar o desconto de 10%

# Exibição dos resultados
print(f"Para uma compra de {quantidade_compra_morango:.2f} kg de morango e {quantidade_compra_maca:.2f} kg de maçã, o valor a ser pago pela pessoa cliente será R$ {valor_total_compra:.2f}")

