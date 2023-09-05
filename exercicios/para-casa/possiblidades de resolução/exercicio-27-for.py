def calcula_preco(fruta):
    if fruta['peso'] > fruta['peso_minimo_para_desconto']: 
        custo = fruta['peso'] * fruta['preco_desconto']
    else: 
        custo = fruta['peso'] * fruta['preco_inteiro']
    return custo

frutas = {
    "macas": {
        "preco_inteiro": 1.8,
        "preco_desconto": 1.5,
        "peso_minimo_para_desconto": 5,
    },
    "morangos": {
        "preco_inteiro": 2.5,
        "preco_desconto": 2.2,
        "peso_minimo_para_desconto": 8
    }
}

custo_total = 0
peso_total = 0
for nome, valores in frutas.items(): 
    valores["peso"] =  float(input("Informe o numero de kilos de {nome}: "))
    peso_total += valores["peso"] 
    custo_total += calcula_preco(valores)

if peso_total > 8 or custo_total > 25:
    custo_total = custo_total * 0.9

print(f"Custo total: {custo_total}")