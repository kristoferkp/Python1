kuu = str(input("Esita kuu: "))

fail = open(kuu + ".txt", encoding = "UTF-8")
andmed = []
for rida in fail:
    andmed.append(rida.strip())
fail.close()

sisse = 0
valja = 0

for i in andmed:
    
    i = float(i)
    
    if i > 0:
        sisse = sisse + i
    elif i < 0:
        valja = valja + i
        
valja = abs(valja)
        
print("Sissetulekute summa: " + str(sisse) + " eurot")
print("Väljatulekute summa: " + str(valja) + " eurot")


if sisse > valja:
    print("Selles kuus oled plussis")
elif sisse == valja:
    print("Selles kuus oled nullis")
elif sisse < valja:
    print("Selles kuus oled miinuses")