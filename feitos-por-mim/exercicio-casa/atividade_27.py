
import math
#pedir a quantidade de morangos e maças, separadas

quant_morangos = float(input("Insira aqui o quilo de morango que deseja: "))
quant_macas = float(input("Insira aqui o quilo de maçãs que deseja: "))

#definir o valor para 5kg e acima de 5kg, cada. 

valor_5kg_morangos = 2.50
valor_5kg_macas = 1.80 
valor_acima_5kg_morangos = 2.20
valor_acima_5kg_macas = 1.50

if quant_morangos <= 5: 
    total_valor_morangos = quant_morangos * valor_5kg_morangos
else: 
    total_valor_morangos = quant_morangos * valor_acima_5kg_morangos



if quant_macas <= 5: 
    total_valor_macas = quant_macas * valor_5kg_macas
else: 
    total_valor_macas = quant_macas * valor_acima_5kg_macas

total_sem_desconto = total_valor_macas + total_valor_morangos

#agora com desconto 

if (quant_macas + quant_morangos) >= 8 or total_sem_desconto >= 25.00:
    aplica_desconto = 0.10 
    total_valor_com_desconto = total_sem_desconto * (1- aplica_desconto)
                                                    #Podemos colocar 0.90, já que queremos 10% de desconto, se fosse 20% de desconto seria 0.80 e assim por diante, (valor total - o desconto.(ta confuso mas faz sentido na minha cabeça kk))


else: 
    total_valor_com_desconto = total_sem_desconto



print(f"O valor total dá igual a R${total_valor_com_desconto:.2f}")

