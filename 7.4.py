from math import ceil

def tordi_kogus(kogus, inimesteArv):
    return ceil(kogus * inimesteArv / 1000)

failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, "r", encoding="UTF-8")
sisu = str(fail.read())
fail.close()

inimesteArv = int(sisu.count("jah"))

print("Tordi tellimisel tuleb arvestada " + str(inimesteArv) + " inimesega.")

print("Tavalist torti on vaja " + str(tordi_kogus(150, inimesteArv)) + " kg.")
print("Marjaželee kattega torti on vaja " + str(tordi_kogus(200, inimesteArv)) + " kg.")