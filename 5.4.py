failiNimi = str(input("Esita faili nimi: "))

fail = open(failiNimi, encoding = "UTF-8")
raamatud = []
for rida in fail:
    raamatud.append(rida.strip())
fail.close()

print("Audioraamatute valik: \n")

for index, raamat in enumerate(raamatud, start = 1):
    print(index, ".", raamat)

raamatuNr = int(input("Mitmendat raamatud soovite lugeda? "))

print(str(raamatuNr), ". raamat on ", raamatud[raamatuNr - 1])