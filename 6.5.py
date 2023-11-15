failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, encoding = "UTF-8")
hinded = []
for rida in fail:
    hinded.append(int(rida.strip()))
fail.close()

def hinnete_keskmine(hinded):
    kokku = 0
    if hinded.count(1) > 0 or hinded.count(2) > 0:
        return -1
    else:
        for hinne in hinded:
            kokku += int(hinne)
        return round(kokku / len(hinded), 1)
    
if hinnete_keskmine(hinded) == -1:
    print("Õpilasel on mitterahuldavaid hindeid")
else:
    print("Hinnete keskmine on " + str(hinnete_keskmine(hinded)))