preco_maca_ate_5kg = 1.8
preco_maca_acima_5kg = 1.5

preco_morango_ate_5kg = 2.5
preco_morango_acima_5kg = 2.2

kgs_de_maca = float(input("Informe o numero de kilos de maca: "))
kgs_de_morango = float(input("Informe o numero de kilos de morango: "))

if kgs_de_maca > 5:
    custo_macas = kgs_de_maca * preco_maca_acima_5kg
else:
    custo_macas = kgs_de_maca * preco_maca_ate_5kg

if kgs_de_morango > 8:
    custo_morangos = kgs_de_morango * preco_morango_acima_5kg
else:
    custo_morangos = kgs_de_morango * preco_morango_ate_5kg

custo_total = custo_macas + custo_morangos

if kgs_de_maca + kgs_de_morango > 8 or custo_total > 25:
    custo_total = custo_total * 0.9

print(f"Custo total: {custo_total}")