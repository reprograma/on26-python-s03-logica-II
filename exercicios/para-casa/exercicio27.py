# Descobrir qual fruta o cliente deseja comprar
tipo_da_fruta = input("Olá! Bem-vindo ao Sacolão da Mari C.! No momento estamos com um estoque pouco variado e temos somente Maçãs e Morangos! Por favor, nos informe qual fruta deseja comprar, digitando 1 para morangos ou 2 para maçãs: ")

# Descobrir quanto de fruta o cliente deseja comprar
quantidade_da_fruta = float(input("Muito bem! Agora nos indique, por favor, a quantidade que deseja comprar: [ATENÇÃO! Note que o nosso sistema calculará a quantidade medida em KG e o valor deverá ser inserido utilizando . ao invés de , caso seja decimal] "))

# Descobrir o valor total da compra considerando a variação de preço em relação ao peso e ao tipo da fruta
preco_morango_menorque5 = 2.50
preco_morango_maiorque5 = 2.20

preco_maca_menorque5 = 1.80
preco_maca_maiorque5 = 1.50

## Se a fruta for Morango (1):
 #Se for menos que 5kg
if tipo_da_fruta == "1" and quantidade_da_fruta < 5:
    preco_bruto_mor_menor5 = (quantidade_da_fruta * preco_morango_menorque5)
    preco_total_mor = preco_bruto_mor_menor5
    print ("O valor da sua compra de " + format(str(quantidade_da_fruta)) + " kilos de morangos será de R$ " + format(str(preco_total_mor)))

 #Se for mais que 5kg
elif tipo_da_fruta == "1" and quantidade_da_fruta > 5:
    preco_bruto_mor_maior5 = (quantidade_da_fruta * preco_morango_maiorque5)

 # Se tem desconto por peso
    if quantidade_da_fruta >= 8:
        preco_total_mor = (preco_bruto_mor_maior5 * 0.9)

 # Se tem desconto por valor
    if preco_bruto_mor_maior5 >= 25:
        preco_total_mor = (preco_bruto_mor_maior5 * 0.9)
    print ("O valor da sua compra de " + format(str(quantidade_da_fruta)) + " kilos de morangos será de R$ " + format(str(preco_total_mor)))

## Se a fruta for Maca (2):
 #Se for menos que 5kg
if tipo_da_fruta == "2" and quantidade_da_fruta < 5:
    preco_bruto_mac_menor5 = (quantidade_da_fruta * preco_maca_menorque5)
    preco_total_mac = preco_bruto_mac_menor5
    print ("O valor da sua compra de " + format(str(quantidade_da_fruta) + " kilos de morangos será de R$ " + str(preco_total_mac)))    

 #Se for mais que 5kg
elif tipo_da_fruta == "2" and quantidade_da_fruta > 5:
    preco_bruto_mac_maior5 = (quantidade_da_fruta * preco_maca_maiorque5)
    print(preco_bruto_mac_maior5)

 # Se tem desconto por peso
    if quantidade_da_fruta >= 8:
        preco_total_mac = (preco_bruto_mac_maior5 * 0.9)

 # Se tem desconto por valor
    if preco_bruto_mac_maior5 >= 25:
        preco_total_mac = (preco_bruto_mac_maior5 * 0.9)
    print ("O valor da sua compra de " + format(str(quantidade_da_fruta)) + " kilos de morangos será de R$ " + format(str(preco_total_mac)))
