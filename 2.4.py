pakiKorgus = int(input("Esita paki kõrgus: "))
pakiKaal = float(input("Esita paki kaal: "))


if pakiKorgus <= 9 and pakiKorgus > 0:
    print("Pakk on S-suurusega ja saab saata pakiautomaadist.")
elif pakiKorgus <= 19 and pakiKorgus > 0:
    print("Pakk on M-suurusega ja saab saata pakiautomaadist.")
elif pakiKorgus <= 39 and pakiKorgus > 0:
    print("Pakk on L-suurusega ja saab saata pakiautomaadist.")
else:
    if pakiKaal > 30:
        print("Pakki saab saata ainult postkontorist.")
    else: 
        print("Pakki saab saata postkontorist või kulleriga.")    