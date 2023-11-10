fail = open("kiirused.txt", encoding = "UTF-8")
kiirused = []
for rida in fail:
    kiirused.append(float(rida.strip()))
fail.close()

for i in kiirused:
    if i >= 20.8 and i <= 24.4:
        print(i)