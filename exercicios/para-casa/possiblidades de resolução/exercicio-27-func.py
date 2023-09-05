def calcula_preco(kilos, preco_inteiro, preco_desconto, minimo_para_desconto):
    if kilos > minimo_para_desconto: 
        custo = kilos * preco_desconto
    else: 
        custo = kilos * preco_inteiro
    return custo

preco_maca_ate_5kg = 1.8
preco_maca_acima_5kg = 1.5
peso_minimo_desconto_maca = 5

preco_morango_ate_5kg = 2.5
preco_morango_acima_5kg = 2.2
peso_minimo_desconto_morango = 8

kgs_de_maca = float(input("Informe o numero de kilos de maca: "))
kgs_de_morango = float(input("Informe o numero de kilos de morango: "))

custo_macas = calcula_preco(kgs_de_maca, preco_maca_ate_5kg, preco_maca_acima_5kg, peso_minimo_desconto_maca)
custo_morangos = calcula_preco(kgs_de_morango, preco_morango_ate_5kg, preco_morango_acima_5kg, peso_minimo_desconto_morango)

custo_total = custo_macas + custo_morangos

if (kgs_de_maca + kgs_de_morango) > 8 or custo_total > 25:
    custo_total = custo_total * 0.9

print(f"Custo total: {custo_total}")