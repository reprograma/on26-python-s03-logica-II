morango_kg = float(input('Quantos Kg de morango? '))
maca_kg = float(input('Quantos Kg de maçã? '))

if morango_kg <= 5:
    preco_morango = 2.5
else:
    preco_morango = 2.2

if maca_kg <= 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5

total_kg = morango_kg + maca_kg
total_valor = (morango_kg * preco_morango) + (maca_kg * preco_maca)

if total_kg > 8 or total_valor > 25:
    total_valor *= 0.9

print(f'O valor do morango é R$ {morango_kg * preco_morango:.2f}')
print(f'O valor da maçã é R$ {maca_kg * preco_maca:.2f}')
print(f'O valor a ser pago é R$ {total_valor:.2f}')