# Exercicio 27 da semana 03 (enuciado muito grande para caber)



def calcular_valor_frutas(kg_morangos, kg_macas):
    preco_morango = 2.50 if kg_morangos <= 5 else 2.20
    preco_maca = 1.80 if kg_macas <= 5 else 1.50
    
    total_sem_desconto = (preco_morango * kg_morangos) + (preco_maca * kg_macas)
    
    if (kg_morangos + kg_macas) > 8 or total_sem_desconto > 25:
        desconto = 0.10 * total_sem_desconto
        total_com_desconto = total_sem_desconto - desconto
    else:
        desconto = 0
        total_com_desconto = total_sem_desconto
    
    return total_com_desconto

# Quantidades de morangos e maçãs
kg_morangos = float(input("Insira a quantidade (em Kg) de morangos:"))
kg_macas = float(input("Insira a quantidade (em Kg) de maçãs:"))


# Cálculo e valor para ser pago 
valor_total = calcular_valor_frutas(kg_morangos, kg_macas)
print(f"O valor a ser pago é R$ {valor_total:.2f}")




