

kgMorango = float(input("Quantos kg de morango? "))
kgMaca = float(input("Quantos kg de maça? "))

valorMorango = 2.5 if kgMorango <= 5 else 2.2
valorMaca = 1.8 if kgMaca <= 5 else 1.5

valorTotal = (valorMorango * kgMorango) + (valorMaca * kgMaca)


#SE O CLIENTE COMPRAR MAIS DE 8KG EM FRUTAS OU O VALOR TOTAL ULTRAPASSAR 25 REAIS, HÁ UM DESCONTO DE 10%
if (kgMorango + kgMaca) > 8 or valorTotal > 25:
    desconto = 0.1 * valorTotal
    valorDesconto = valorTotal - desconto
else:
    valorDesconto = valorTotal

print("Valor total da compra abaixo:")
print(valorTotal)







