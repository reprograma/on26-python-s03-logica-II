print("Seja bem-vindo(a) ao Sacolão Marias")

comp_mor = input("Você vai comprar morango? ")
if comp_mor == "sim":
    mor_kg = int(input ("Quantos Kg? "))
    if mor_kg <= 5:
        total_mor = mor_kg * 2.50
    else: 
        total_mor = mor_kg * 2.20
else:
    mor_kg = 0
    total_mor = 0

comp_mac = input("Você vai comprar maça? ")
if comp_mac == "sim":
    mac_kg = int(input("Quantos Kg? "))
    if mac_kg <= 5:
        total_mac = mac_kg * 1.80
    else: 
        total_mac = mac_kg * 1.50
else:
    mac_kg = 0
    total_mac = 0

total_kg = mor_kg + mac_kg
valor_comp = float(total_mor + total_mac)

if total_kg > 8:
    pagamento = (total_mor + total_mac)*0.90
elif valor_comp > 25:
    pagamento = (total_mor + total_mac)*0.90
else: 
    pagamento = (total_mor + total_mac)

print("O valor a ser pago será " + str("%.2f" % pagamento))