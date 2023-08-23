
#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                     # Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
#receberá ainda um desconto de 10% sobre este total. 
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.

quantidade_de_morango = float(input("Quantos morangos deseja comprar?",))
quantidade_de_maca = float(input("Quantas macãs deseja comprar?",))
quantidade_de_frutas = quantidade_de_morango + quantidade_de_maca


if quantidade_de_morango <= 5:
    preco_do_morango = 2.50
else:
    preco_do_morango = 2.20     

if quantidade_de_maca <= 5:
    preco_da_maca = 1.80
else:
    preco_da_maca = 1.50

    
def total_a_ser_pago_frutas(quantidade_de_morango, preco_morango, quantidade_de_maca, preco_maca):
    valor_da_compra = quantidade_de_morango * preco_morango + quantidade_de_maca*preco_maca
    return valor_da_compra


total = total_a_ser_pago_frutas(quantidade_de_morango, preco_do_morango, quantidade_de_maca, preco_da_maca)
if quantidade_de_frutas <= 8 and total <= 25:
    print(f"O preço total da sua compra é de R$ {total:.2f}")   
else:
    print(f"O preço total da sua compra é de R$ {total*0.9:.2f}")