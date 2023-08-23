# Exercício de Casa 🏠 
#### Exercício de Estrutura de decisão 
https://wiki.python.org.br/EstruturaDeDecisao
Exercício 27. 

---
#Uma fruteira está vendendo frutas com a seguinte tabela de preço
# Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este
#total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

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
