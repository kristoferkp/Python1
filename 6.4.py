def täishäälikud(sona):
    return sona.count("a") + sona.count("e") + sona.count("i") + sona.count("o")  + sona.count("u")  + sona.count("ä")  + sona.count("ü")  + sona.count("ö")  + sona.count("õ")

sona = input("Sisesta sõna: ")

print("Sõnas", sona, "on täishäälikuid", str(täishäälikud(sona)))