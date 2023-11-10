kordused = int(input("Esita mitmene poolik püramiid on: "))
arv = 0
n = 0
while kordused > 0:
    n = n + 1
    arv = arv + n
    kordused = kordused - 1
print(arv)