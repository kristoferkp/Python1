from random import randint

pudeliteArv = int(input("Esita limonaadipudelite arv: "))
voidugaPudeliteArv = 0

while pudeliteArv > 0:
    arv = randint(1, 3)
    if arv == 3:
        print("Osteti limonaad, millega võideti uus limonaad!")
        voidugaPudeliteArv += 1
    else:
        print("Osteti limonaad.")
    pudeliteArv = pudeliteArv - 1
print(voidugaPudeliteArv)