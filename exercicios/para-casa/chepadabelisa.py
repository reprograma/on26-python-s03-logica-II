def calcular_preco(peso, preco_comum, preco_desconto):
  total_fruta = peso * preco_comum
  if peso > 5:
    total_fruta = peso * preco_desconto
    
  return total_fruta
    
def preco_total(precomorango, precomaca, quantidade1, quantidade2):
      total_da_compra = precomorango + precomaca
      peso = quantidade1 + quantidade2
      if total_da_compra > 25 or peso > 8:
            total_da_compra = total_da_compra * 0.9
      return total_da_compra
      
quantidade1 = float(input("Digite a quantidade em KG de Morango -> "))
quantidade2 = float(input("Digite a quantidade em KG de Maça -> "))

#Valores até 5KG
morango = 2.50
maca = 1.80
#Valores acima de 5KG
morango2 = 2.20
maca2 = 1.50

precomorango = calcular_preco(quantidade1, morango, morango2)
precomaca = calcular_preco(quantidade2, maca, maca2)
total_bruto = preco_total(precomorango, precomaca, quantidade1, quantidade2)
print("O total da sua compra deu " + str(total_bruto))