

pesokgclt_morango = float(input("Quantos kgs. de morango você deseja? "))
pesokgclt_maca = float(input("Quantos kgs. de maça você deseja? "))

if pesokgclt_morango <= 5: 
    vlr_morango = 2.5
else:
    vlr_morango = 2.2

if pesokgclt_maca <= 5:
    vlr_maca = 1.8
else:
    vlr_maca = 1.5


valor_ttl = pesokgclt_morango * vlr_morango + pesokgclt_maca * vlr_maca
total_kgs = pesokgclt_morango + pesokgclt_maca

if total_kgs > 8 or valor_ttl > 25:
    print(f"Você ganhou um desconto de 10%, pagará apenas {valor_ttl * 0.9:.2f} por suas frutas")
else:
    print(f"Você pagará R$ {valor_ttl:.2f} por suas frutas.")