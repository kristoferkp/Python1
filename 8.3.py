failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, "r", encoding="UTF-8")

andmed = []
for i in fail:
    andmed.append(i.strip())
    
fail.close()

def tüüp(arv):
    
    if arv > 25000:
        return "FFP1"
    elif arv > 5000:
        return "FFP2"
    elif arv <= 5000:
        return "FFP3"

kokku = 0

for i in andmed:
    if tüüp(int(i)) == "FFP3" or tüüp(int(i)) == "FFP2":
        kokku += 1
        
print("FFP2 ja FFP3 tüüpi maske oli kokku " + str(kokku) + ".")