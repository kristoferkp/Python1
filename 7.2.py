failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, "r", encoding = "UTF-8")
sisu = str(fail.read())
fail.close()

sisu = sisu.replace('\n', ' ')

uusFailiNimi = input("Sisesta uue faili nimi: ")
uusFail = open(uusFailiNimi, "w", encoding = "UTF-8")
uusFail.write(sisu)
uusFail.close()