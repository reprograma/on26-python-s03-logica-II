quantidade1 = float(input("Digite a quantidade em KG de Morango -> "))
quantidade2 = float(input("Digite a quantidade em KG de Maça -> "))

#Valores até 5KG
morango = 2.50
maca = 1.80

#Valores acima de 5KG
morango2 = 2.20
maca2 = 1.50

def calcular_preco(p1, p2):
  if p1 + p2 > 5:
        return(p1 * morango2) + (p2 * maca2)
  else: 
        return(p1 * morango) + (p2 * maca)
    
preco = calcular_preco(quantidade1, quantidade2)

print("VALOR TOTAL R$: " + str(preco))