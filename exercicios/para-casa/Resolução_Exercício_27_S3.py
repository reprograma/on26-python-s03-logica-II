# Resolução exercício para casa - Questão 27

## Link de acesso: https://wiki.python.org.br/EstruturaDeDecisao 


### 1° passo

quant_kg_morango = float(input('Digite o valor (kg) de morango: '))
quant_kg_maca = float(input("Digite o valor(kg) de maça: "))

### 2° passo

if quant_kg_morango <=5:
    valor_morango = quant_kg_morango * 2.5

else: 
    valor_morango = quant_kg_morango * 2.2

if quant_kg_maca <=5 :
    valor_maca = quant_kg_maca * 1.80

else:
    valor_maca = quant_kg_maca * 1.5

### 3° passo

valor_total_kg = quant_kg_morango + quant_kg_maca  

valor_total_reais = valor_morango + valor_maca 


if valor_total_kg >8 or valor_total_reais >25:
    valor_final = valor_total_reais - (valor_total_reais * 0.1) 

else:
    valor_final = valor_total_reais

print(valor_final)



    