fail = open("nimed.txt", encoding = "UTF-8")
nimed = []
for rida in fail:
    nimed.append(rida.strip())
fail.close()

jarjekorraNr = int(input("Mitmendat nime soovid? "))

print(str(jarjekorraNr), '. nimi on ', nimed[jarjekorraNr - 1])