def calcula_preco(kilos, info):
    if kilos > info['peso_minimo_para_desconto']: 
        custo = kilos * info['preco_desconto']
    else: 
        custo = kilos * info['preco_inteiro']
    return custo

info_macas = {
        "preco_inteiro": 1.8,
        "preco_desconto": 1.5,
        "peso_minimo_para_desconto": 5
    }
    
info_morangos = {
        "preco_inteiro": 2.5,
        "preco_desconto": 2.2,
        "peso_minimo_para_desconto": 8
    }


kgs_de_maca = float(input("Informe o numero de kilos de maca: "))
kgs_de_morango = float(input("Informe o numero de kilos de morango: "))

custo_macas = calcula_preco(kgs_de_maca, info_macas)
custo_morangos = calcula_preco(kgs_de_morango, info_morangos)

custo_total = custo_macas + custo_morangos

if (kgs_de_maca + kgs_de_morango) > 8 or custo_total > 25:
    custo_total = custo_total * 0.9

print(f"Custo total: {custo_total}")