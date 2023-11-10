puramiidiSuurus = int(input("Esita püramiidi suurus: "))
kokku = 0
arv = 0
i = 1

while i <= (puramiidiSuurus * 2 - 1):
    if puramiidiSuurus >= i:
        arv += 1
        kokku += arv
        i += 1
    elif puramiidiSuurus < i:
        arv -= 1
        kokku += arv
        i += 1
        
print(kokku)