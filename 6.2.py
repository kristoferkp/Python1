hind = float(input("Sisesta elektrihind sentides kilovatt-tunni kohta: "))

def elektrihind(hind):
    return hind * 10

print(str(hind) + " s/kWh on " + str(elektrihind(hind)) + " €/MWh")