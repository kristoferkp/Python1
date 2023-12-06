failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, "r", encoding="UTF-8")
andmed = []
for i in fail:
    andmed.append(i.strip())
fail.close()

def vitamiin_D(seerum):
    """
    Calculate the recommended vitamin D dosage based on the serum level.

    Parameters:
    seerum (float): The serum level of vitamin D.

    Returns:
    int: The recommended vitamin D dosage in micrograms.
    """
    if seerum > 75:
        return 20
    elif seerum > 50 and seerum <= 75:
        return 35
    elif seerum > 25 and seerum <= 50:
        return 50
    elif seerum <= 25:
        return 100

inimesteArv = 0

for i in andmed:
    if float(i) > 75:
        inimesteArv += 1
    print("Tase: " + i + " nmol/l - Vitamiin D annus: " + str(vitamiin_D(float(i))) + " mikrogrammi")
   
print("Normaalse vitammiin D tasemega inimeste arv: " + str(inimesteArv))