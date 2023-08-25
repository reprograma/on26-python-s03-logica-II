# Cálculo dos valores a serem pagos por um cliente que compra morangos em uma fruteira
# Se o cliente comprar até 5kg de morango o valor será de R$ 1.80/kg
# Se o cliente comprar acima de 5kg de morango, o valor será de R$ 1.50/kg
# Se o cliente comprar mais de 8kg de morango ou se o valor da compra ultrassar R$ 25.00, ele terá 10% de desconto
# Este programa solicita a quantidade (em kg) de morangos a ser comprada e calcula o valor da respectiva compra

maca_ate_5_kg = 1.80
preco_da_maca_acima_5_kg = 1.50

#Função que calcula o valor da compra a partir da quantidade de morangos desejada, \
# sem considerar os possíveis descontos:

def compra_de_macas (quantidade, preco):
    valor_compra = round((quantidade*preco), 2)
    return(valor_compra)


quantidade_em_kilo = float(input("Informe o peso das maçãs em kg "))
preco_ate_5kg = 1.80
preco_acima_5kg = 1.50

retorno_valor_ate_5kg = compra_de_macas (quantidade_em_kilo, preco_ate_5kg)
retorno_valor_acima_5kg = compra_de_macas (quantidade_em_kilo, preco_acima_5kg)

if quantidade_em_kilo <= 5.0:
    print("Valor a ser pago pelo cliente ")
    print(retorno_valor_ate_5kg)
elif quantidade_em_kilo > 5.0 and quantidade_em_kilo <= 8.0:
    print("Valor a ser pago pelo cliente ")
    print(retorno_valor_acima_5kg)
elif quantidade_em_kilo > 8.0 or retorno_valor_acima_5kg > 25.0:
    print("Valor a ser pago pelo cliente")
    print((retorno_valor_acima_5kg)-(retorno_valor_acima_5kg*0.10))