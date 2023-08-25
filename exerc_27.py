# Cálculo dos valores a serem pagos por um cliente que compra morangos em uma fruteira
# Se o cliente comprar até 5kg de morango o valor será de R$ 2.50/kg
# Se o cliente comprar acima de 5kg de morango, o valor será de R$ 2.20/kg
# Se o cliente comprar mais de 8kg de morango ou se o valor da compra ultrassar R$ 25.00, ele terá 10% de desconto
# Este programa solicita a quantidade (em kg) de morangos a ser comprada e calcula o valor da respectiva compra

preco_do_morango_ate_5_kg = 2.50
preco_do_morango_acima_5_kg = 2.20

#Função que calcula o valor da compra a partir da quantidade de morangos desejada, \
# sem considerar os possíveis descontos:

def compra_de_morangos (quantidade, preco):
    valor_compra = round((quantidade*preco), 2)
    return(valor_compra)


quantidade_em_kilo = float(input("Informe o peso dos morangos em kg "))
preco_ate_5kg = 2.50
preco_acima_5kg = 2.20

retorno_valor_ate_5kg = compra_de_morangos (quantidade_em_kilo, preco_ate_5kg)
retorno_valor_acima_5kg = compra_de_morangos (quantidade_em_kilo, preco_acima_5kg)

if quantidade_em_kilo <= 5.0:
    print("Valor a ser pago pelo cliente ")
    print(retorno_valor_ate_5kg)
elif quantidade_em_kilo > 5.0 and quantidade_em_kilo <= 8.0:
    print("Valor a ser pago pelo cliente ")
    print(retorno_valor_acima_5kg)
elif quantidade_em_kilo > 8.0 or retorno_valor_acima_5kg > 25.0:
    print("Valor a ser pago pelo cliente")
    print((retorno_valor_acima_5kg)-(retorno_valor_acima_5kg*0.10))