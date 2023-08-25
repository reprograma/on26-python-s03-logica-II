
#qual a quantidade de morangos adquirida pelo cliente, em KG
quantidade_de_morango= float(input("Digite a quantidade de morango em kg=  "))

#qual a quantidade de maçãs adquirida pelo cliente, em KG
quantidade_maca= float(input("Digite a quantidade de maçãs=  "))

#calcular o valor a ser pago pelos morangos
if quantidade_de_morango <5:
    valor_pago_morango = quantidade_de_morango*2.50
else:
    valor_pago_morango = quantidade_de_morango*2.20

#calcular o valor a ser pago pelas maçãs
if quantidade_maca <5:
    Valor_pago_maca = quantidade_maca*1.80
else:
    Valor_pago_maca = quantidade_maca*1.50

#calcular o valor total 
valor_total= Valor_pago_maca+valor_pago_morango

quantidade_final= quantidade_de_morango+quantidade_maca

#aplicar o desconto
if quantidade_final >8 or valor_total >25:
    valor_final = (valor_total*0.9)
    print(f"O valor final é de {valor_final:.2f} reias")
else:
    print(f"O valor final é de {valor_total:.2f} reias")