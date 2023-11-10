failiNimi = input("Sisesta faili nimi: ")
fail = open(failiNimi, encoding = "UTF-8")
sisu = str(fail.read())
fail.close()

sisu = sisu.replace('8', 'ö')
sisu = sisu.replace('2', 'ä')
sisu = sisu.replace('6', 'õ')
sisu = sisu.replace('y', 'ü')

print(sisu)