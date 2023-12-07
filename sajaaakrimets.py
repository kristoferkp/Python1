def juurdekasv(pindala, juurdekasv):
    return round(pindala * 0.4047 * juurdekasv, 2)

failinimi = input("Sisestage failinimi: ")
juurdekasv_hektari_kohta = float(input("Sisestage puuliigi aastane juurdekasv tihumeetrites: "))
piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))

arvutatud_juurdekasv = 0
with open(failinimi, 'r') as file:
    for line in file:
        pindala = float(line.strip())
        if pindala > piir:
            aastane_juurdekasv = juurdekasv(pindala, juurdekasv_hektari_kohta)
            print(f"Metsatüki aastane juurdekasv: {aastane_juurdekasv}")
            arvutatud_juurdekasv += 1
        else:
            print("Metsatükki ei võeta arvesse")

print(f"Kokku arvutati {arvutatud_juurdekasv} metsatüki juurdekasv.")
