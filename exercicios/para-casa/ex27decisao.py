print('Venda de frutas')
pesoMo = float(input('Informe quantos quilos de morango:'))
pesoMa = float(input('Informe quantos quilos de maçã:'))
valorMo1 = 2.2 * pesoMo
valorMo2 = 2.5 * pesoMo
valorMa1 = 1.5 * pesoMa
valorMa2 = 1.8 * pesoMa
pesoT = pesoMo + pesoMa
valorT1 = valorMo1 + valorMa1
valorT2 = valorMo1 + valorMa2
valorT3 = valorMo2 + valorMa1
valorT4 = valorMo2 + valorMa2

if pesoMo <= 5.00 and pesoMa <= 5.00:
    print("Valor total: ", valorT4)
elif pesoMo > 5.00 and pesoMa <= 5.00:
    print("Valor total; ", valorT3)
elif pesoMo <= 5.00 and pesoMa > 5.00:
    print("Valor total: ", valorT2)
elif pesoMo > 5.00 and pesoMa > 5.00:
    print("Valor total: ", valorT1)

if pesoT > 8.00 or valorT1 > 25.00 or valorT2 > 25.00 or valorT3 > 25.00 or valorT4 > 25.00:
    valorT = valorT1, valorT2, valorT3, valorT4
    print("Desconto! Novo valor total = R$ ", (0.9 * valorT))