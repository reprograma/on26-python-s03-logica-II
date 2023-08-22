# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da 
# compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% 
# sobre este total. Escreva um algoritmo para ler a quantidade 
# (em Kg) de morangos e a quantidade (em Kg)de maças adquiridas
# e escreva o valor a ser pago pelo cliente.

#passar os pesos das frutas 


#veriáveis

preco_morango_por_kg_ate_5kg = 2.50
preco_maca_por_kg_ate_5kg = 1.80 
preco_morango_por_kg_acima_5kg = 2.20   
preco_maca_por_kg_acima_5kg = 1.50 


#ações

print( "Digite a quantidade de morango que deseja comprar" )
morangos_kg= float(input())
print( "Digite a quantidade de morango que deseja comprar" )
maca_kg = float(input())

total_kg_morango_maca = morangos_kg + maca_kg
total_compra = 0


if morangos_kg < 5 :
        valor_total  = preco_morango_por_kg_ate_5kg * morangos_kg
else:
        valor_total =  preco_maca_por_kg_acima_5kg * morangos_kg
if maca_kg < 5 : 
        valor_total  = preco_maca_por_kg_ate_5kg * maca_kg
    
else:
            valor_total =  preco_maca_por_kg_acima_5kg * maca_kg
    
    
    # condião para ganhafr o descontoelse:
    
if total_kg_morango_maca > 8 or total_compra > 25  :
        desconto = 0.9
        valor_total = valor_total * 0.9
        print( " Desconto de 10% aplicado")
else:
    valor_total = (preco_morango_por_kg_ate_5kg * morangos_kg) + (preco_maca_por_kg_ate_5kg * maca_kg)
    print( " Desconto de 10% não aplicado")

print("A quantidade total de frutas é: ", total_kg_morango_maca, " e o  valor a ser pago é  ", valor_total)