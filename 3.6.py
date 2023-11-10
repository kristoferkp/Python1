investeeritavSumma = float(input("Esita investeeritav summa: "))
investeeringuPikkus = int(input("Esita investeeringu kogupikkus aastates: "))
aastatootlus = float(input("Esita oodatav aastatootlus protsentides: "))

while investeeringuPikkus > 0:
    investeeritavSumma = investeeritavSumma + investeeritavSumma * aastatootlus / 100
    investeeringuPikkus -= 1

print(round(investeeritavSumma, 2))