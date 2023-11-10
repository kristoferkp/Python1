temperatuur = int(input("Esita välistemperatuur: "))
paike = str(input("Kas päike pastab? ('jah' või 'ei'): "))
rohelineLipp = str(input("Kas rannas on roheline lipp? ('jah' või 'ei'): "))

if rohelineLipp == 'jah' or temperatuur >= 20 and paike == 'jah':
    print("Võid minna randa!")
elif rohelineLipp == 'ei' or temperatuur < 20 or paike == 'ei':
    print("Täna ei tasu randa minna.")
else:
    print("Vale sisend!")