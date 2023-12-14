failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, "r", encoding="UTF-8")
andmed= []

for i in fail:
    andmed.append(int(i.strip()))
    
fail.close()

def kalorid(basseiniOtsad, pikkus):
    return round(basseiniOtsad * pikkus / 1000 * 120, 1)

basseiniPikkus = int(input("Sisesta basseini otsa pikkus meetrites: "))

kokku = 0

for i in andmed:
    i = kalorid(i, basseiniPikkus)
    print("Kaloreid kulus: " + str(i))
    kokku += i

print("Kokku kulus: " + str(kokku) + " kalorit.")