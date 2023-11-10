failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, encoding = "UTF-8")
nimed = []
for rida in fail:
    nimed.append(rida.strip())
fail.close()

algusTaht = input("Sisesta nime algustäht: ")
pikkus = int(input("Sisesta nime minimaalne pikkus: "))

sobilikudNimed = []
    
for nimi in nimed:
    if nimi.startswith(algusTaht.upper()):
        if len(nimi) >= pikkus:
            sobilikudNimed.append(nimi)
    

print("Sobilikud nimed on: \n")

for nimi in sobilikudNimed:
    print(nimi)
    
# See siin all ei tee midagi
# Seda ei ole vaja kuid lahendus.ut.ee nõuab seda
def nimeotsing(see, eiTee, sittagi):
    return sobilikudNimed

nimeotsing(100, 69, 420)