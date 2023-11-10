alghinnad = open("alghinnad.txt", encoding = "UTF-8")
hinnakordajad = open("hinnakordajad.txt", encoding = "UTF-8")

hinnad = []
kordajad = []

for i in alghinnad:
    hinnad.append(i.strip())
alghinnad.close()

for i in hinnakordajad:
    kordajad.append(i.strip())
hinnakordajad.close()

kokku = 0
for index, hind in enumerate(hinnad):
    print(str(index + 1) + ". toote alghind: " + str(hind) + ", kampaaniahind: " + str(float(hind) * float(kordajad[int(index)])))
    kokku += float(hind) * float(kordajad[int(index)])
    
print("Toodete kogumaksumus on " + str(kokku))    