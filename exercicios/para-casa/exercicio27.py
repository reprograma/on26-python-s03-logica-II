# Maçã

preco_ate_5kg = 1.80
preco_acima_5kg = 1.50

numero_kg_maca = float(input())

if numero_kg_maca <= 5:
    preco_macas = numero_kg_maca * preco_ate_5kg
    print(f"o quilo de maçã é menor ou até 5, dando {preco_macas} reais")

else:
    preco_macas = numero_kg_maca * preco_acima_5kg
    print(f"o quilo de maçã é maior que 5, dando {preco_macas} reais")


# Morango

preco_morango_ate5kg = 2.50
preco_morango_acima5kg = 2.20
numero_kg_morango = float(input())

if numero_kg_morango <= 5:
    preco_morangos = numero_kg_morango * preco_morango_ate5kg
    print(f"o quilo de morango é menor ou até 5, dando {preco_morangos} reais")

else:
    preco_morangos = numero_kg_morango * preco_morango_acima5kg
    print(f"o quilo de morango é maior que 5, dando {preco_morangos} reais")

# Mais de oito quilos ou mais que 25 reais em frutas, desconto de 10%
kg_total = numero_kg_maca + numero_kg_morango
print(f"kg total é: {kg_total}")

preco_total = preco_macas + preco_morangos
print(f"preco total é: {preco_total}")

if kg_total > 8:
    valor_final = preco_total - (preco_total * 0.1)
    print(f"valor final 10% pelo peso é: {valor_final}")

elif preco_total > 25:
    valor_final = preco_total - (preco_total * 0.1)
    print(f"valor final 10% pelo preço é: {valor_final}")