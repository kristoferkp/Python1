def raha_eurodes(kastideArv, kiloHind):
    kiloHind = kiloHind / 100
    return round(kastideArv * 5 * kiloHind, 1)


failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, "r", encoding="UTF-8")
andmed= [] # Example file contents 14, 15, 16, 15, 14, 14, 10

for i in fail:
    andmed.append(int(i.strip()))
    
fail.close()

mustikaKiloHind = int(input("Sisesta mustika kilo hind (Sentides): "))

n = 1
kokku = 0

for i in andmed:
    i = raha_eurodes(i, mustikaKiloHind)
    print(f'{n}. päeval sai {i} eurot.')
    kokku += i
    n += 1

print(f"Kokku sai: {kokku} eurot.")
