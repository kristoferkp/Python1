import math

def mitu_ringi(ringiPikkus):
    ringideArv = math.ceil(30 / ringiPikkus)
    return ringideArv

luhem = float(input("Sisesta lühema ringi pikkus: "))
pikem = float(input("Sisesta pikema ringi pikus: "))

print("Lühemat ringi on vaja käia " + str(mitu_ringi(luhem)) + " korda.")
print("Pikemat ringi on vaja käia " + str(mitu_ringi(pikem)) + " korda.")