#Exercício 27. 

---

preco_menos_do_que_5kg = {
    'Morango': 2.5,
    'Maçã': 1.8
}

preco_maior_do_que_5kg = {
    'Morango': 2.2,
    'Maçã': 1.5
}

numero_de_kg_morango = float(input("Quantidade de morangos (em Kg): "))

if numero_de_kg_morango < 5:
    preco_do_morango = numero_de_kg_morango * preco_menos_do_que_5kg['Morango']
else:
    preco_do_morango = numero_de_kg_morango * preco_maior_do_que_5kg['Morango']


numero_de_kg_maca = float(input("Quantidade de maçãs (em Kg): "))

if numero_de_kg_maca < 5:
    preco_da_maca = numero_de_kg_maca * preco_menos_do_que_5kg['Maçã']
else:
    preco_da_maca = numero_de_kg_maca * preco_maior_do_que_5kg['Maçã']


valor_total_kg = numero_de_kg_morango + numero_de_kg_maca

valor_total = preco_do_morango + preco_da_maca

if valor_total_kg > 8 or valor_total > 25:
    valor_final = valor_total * 0.9
else:
    valor_final = valor_total

print(f"Valor total da compra: R$ {valor_final:.2f}")
