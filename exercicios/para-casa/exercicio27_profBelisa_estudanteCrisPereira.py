# Exercicio aula semana 3 - Funções condicionais
def totalProduto (peso_prod, preco_prod, preco_desconto, peso_desconto):
    total_produto = peso_prod*preco_prod

    if peso_prod > peso_desconto:
        total_produto = peso_prod * preco_desconto 

    return total_produto

def totalFinal (peso_prod1, peso_prod2, total_prod1, total_prod2, peso_desconto_extra, total_com_desconto, desconto_extra):
    peso_total = peso_prod1 + peso_prod2
    total_compra = total_prod1 + total_prod2

    if peso_total > peso_desconto_extra or total_compra > total_com_desconto:
        total_compra = total_compra - total_compra*desconto_extra
    
    return total_compra
        
peso_morango = float(input("Insira o peso de morango a ser comprado: "))
peso_maca = float(input("Insira o peso de maçã a ser comprada: "))

preco_morango = 2.5
preco_maca = 1.8
preco_com_desconto_morango = 2.2
preco_com_desconto_maca = 1.5
peso_desconto = 5
peso_desconto_extra = 8
total_compra_com_desconto = 25
desconto_extra = 0.1

total_morango = totalProduto(peso_morango, preco_morango,preco_com_desconto_morango,peso_desconto)
total_maca = totalProduto(peso_maca, preco_maca,preco_com_desconto_maca,peso_desconto)
total_da_compra = totalFinal (peso_morango, peso_maca, total_morango, total_maca, peso_desconto_extra, total_compra_com_desconto, desconto_extra)

print(" ")
print("Extrato")
print(peso_morango, "kg morangos: R$ ", total_morango)
print(peso_maca, "kg maçãs: R$ ",total_maca)
print("Total da compra - com desconto extra se aplicável: R$ ", total_da_compra)