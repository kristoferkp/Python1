from datetime import datetime

tahtpaev = input("Sisesta tähtpäev: ")
kuupaev = input("Sisesta kuupäev: ")

paev = datetime.strptime(kuupaev, "%d.%m.%Y")
paev = paev.isoweekday()

paevad = {
    "1": "esmaspäev",
    "2": "teisipäev",
    "3": "kolmapäev",
    "4": "neljapäev",
    "5": "reede",
    "6": "laupäev",
    "7": "pühapäev"
}
print(paevad[str(paev)])

fail = open("tähtpäevad.txt", "a", encoding="UTF-8")
fail.write("Tähtpäev: " + tahtpaev + "\n")
fail.write("Kuupäev: " + kuupaev + "\n")
fail.write("Nädalapäev on " + paevad[str(paev)] + ".")

fail.close()