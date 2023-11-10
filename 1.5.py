jooksuPunktid = float(input("Esita jooksu tulemus: "))
kaugusPunktid = int(input("Esita kaugushüppe tulemus: "))
jooksuPunktid = 18 - jooksuPunktid
jooksuPunktid = jooksuPunktid ** 1.81
jooksuPunktid = 25.4347 * jooksuPunktid
kaugusPunktid = kaugusPunktid - 220
kaugusPunktid = kaugusPunktid ** 1.4
kaugusPunktid = 0.14354 * kaugusPunktid
kokkuPunkte = int(kaugusPunktid) + int(jooksuPunktid)
print(kokkuPunkte)