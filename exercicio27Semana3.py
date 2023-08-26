#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
 #                     Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da 
# compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos 
# e a quantidade (em Kg) de maças adquiridas 
# e escreva o valor a ser pago pelo cliente.

print ("Olá queride Cliente. Boas Vindas!")
print ("Por favor, informe quantos kg de Morango você comprou? ")
kg_de_morango = float (input())
print ("Por favor, informe quantos Kg de Maçã você comprou?")
kg_de_maca = float (input())

valorMor1 = kg_de_morango * 2.50
valorMor2 = kg_de_morango * 2.20
valorMa1 = kg_de_maca * 1.80
valorMa2 = kg_de_maca * 1.50
valor_total_kg = kg_de_morango + kg_de_maca

if kg_de_morango <= 5.0 and kg_de_maca <= 5.0:
     valor_total_compra =  valorMor1 + valorMa1       
elif kg_de_morango <= 5.0 and kg_de_maca > 5.0:
       valor_total_compra = valorMor1 + valorMa2
elif kg_de_morango > 5.0 and kg_de_maca <= 5.0:
   valor_total_compra = valorMor2 + valorMa1
else: 
    valor_total_compra = valorMor2 + valorMa2
     


valor_total_Desconto = (valor_total_compra - (valor_total_compra * 0.1))

    
if valor_total_compra > 25 or valor_total_kg > 8:
    
   print (f"O valor a ser pago é com Desconto de 10$: R${valor_total_Desconto:.2f}")
else:
   print (f"O valor a ser pago é R${valor_total_compra:.2f}")



