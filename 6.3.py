import math

def mitu_ringi(ringiPikkus):
    # Calculate the number of rings needed to cover a distance of 30 units
    ringideArv = math.ceil(30 / ringiPikkus)
    return ringideArv

# Prompt the user to enter the length of the shorter and longer rings
luhem = float(input("Sisesta lühema ringi pikkus: "))
pikem = float(input("Sisesta pikema ringi pikus: "))

# Calculate and print the number of times the shorter and longer rings need to be walked
print("Lühemat ringi on vaja käia " + str(mitu_ringi(luhem)) + " korda.")
print("Pikemat ringi on vaja käia " + str(mitu_ringi(pikem)) + " korda.")