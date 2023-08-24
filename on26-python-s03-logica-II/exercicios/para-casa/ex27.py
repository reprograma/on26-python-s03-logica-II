#até 5kg
#morango1 = 2,50    
#maca1 = 1,80
#acima de 5kg
#morango2 = 2,20   
#maca2 = 1,50

morango = int(input("Quantos kg de morango?: "))
maca = int(input("Quantos kg de maçãs?: "))

preco_morango1 = morango * 2.50
preco_morango2 = morango * 2.20

preco_maca1 = maca * 1.80
preco_maca2 = maca * 1.50

print("qtd de maçãs: ", maca, "qtd de morangos: ", morango)

if morango > 5:
    preco_correto_morango = preco_morango1
if maca > 5:
    preco_correto_maca = preco_maca1
else:
    preco_correto_maca = preco_maca2
preco_total = preco_correto_maca + preco_correto_morango