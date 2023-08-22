#exercicio27 - estrutura de decisão (python)
# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                   Até 5 Kg              Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$25,00,
#receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
#(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas\
# e escreva o valor a ser pago pelo cliente. 

def compra(n1, n2):
    preco = (n1 + n2)
    return preco

morango_menor_5kg = 2.5
morango_maior_5kg = 2.2
maca_menor_5kg = 1.8
maca_maior_5kg = 1.5

kg_morango = float(input('Digite a quantidade em kg de morangos: '))
kg_maca = float(input('Digite a quantidade em kg de maçãs: '))

if kg_morango < 5:
    preco_morango = kg_morango * morango_menor_5kg
    print(f'Preço dos morangos R$: {preco_morango:.2f}')
elif kg_morango >= 5:
    preco_morango = kg_morango * morango_maior_5kg
    print(f'Preço dos morangos R$: {preco_morango:.2f}')
if kg_maca < 5:
    preco_maca = kg_maca * maca_menor_5kg
    print(f'Preço das maçãs R$: {preco_maca:.2f}')
elif kg_maca >= 5:
    preco_maca = kg_maca * maca_maior_5kg
    print(f'Preço das maçãs R$: {preco_maca:.2f}')

valor_total = compra(preco_morango, preco_maca)

if (kg_morango + kg_maca) > 8 or valor_total > 25:
    preco_com_desconto = valor_total * 0.9
    print(f'O valor total da compra com desconto é R$: {preco_com_desconto:.2f}')
else:
    print(f'O valor total da compra é R$: {valor_total:.2f}, sem desconto')