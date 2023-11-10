from math import ceil

def invest(makse):
    return round(float(ceil(float(makse)) - float(makse)), 2)

failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, "r", encoding="UTF-8")

maksed = []
for i in fail:
    maksed.append(i.strip())
    
fail.close()

investeering = 0

for makse in maksed:
    inv = invest(makse)
    if inv == 0:
        print("Investeeringut ei tehta")
    print(str(inv))
    investeering += round(inv, 2)
    
investeering = round(investeering, 2)
    
print("Investeeringute kogusumma: " + str(investeering) + " eurot.")