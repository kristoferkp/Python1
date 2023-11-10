emaPikkus = int(input("Esita ema pikkus: "))
isaPikkus = int(input("Esita isa pikkus: "))
lapseSugu = str(input("Esita lapse sugu ('M' või 'N'): "))

if lapseSugu == 'M' or lapseSugu == 'm':
    print("Lapse eeldatav pikkus: " + str((emaPikkus + isaPikkus) / 2 + 6.5))    
elif lapseSugu == 'N' or lapseSugu == 'n':
    print("Lapse eeldatav pikkus: " + str((emaPikkus + isaPikkus) / 2 - 6.5))
else:
    print("Vale sisend. Proovi uuesti.")