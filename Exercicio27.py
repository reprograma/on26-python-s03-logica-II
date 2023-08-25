morangos_kg = 10
macas_kg = 10

preco_morango = 0
preco_maca = 0

if morangos_kg <= 5:
    preco_morango = morangos_kg * 2.50
else:
    preco_morango = morangos_kg * 2.20

if macas_kg <= 5:
    preco_maca = macas_kg * 1.80
else:
    preco_maca = macas_kg * 1.50

preco_total = preco_morango + preco_maca

if (morangos_kg + macas_kg) > 8 or preco_total > 25:
    desconto = preco_total * 0.1
    preco_total -= desconto

print(f"Valor total a ser pago: R$ {preco_total:.2f}")