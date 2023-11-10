kordusteArv = int(input("Mitu korda soovite loitsu kasutada? "))
loitsuNimi = input("Sisesta loits: ")
    
def loits(loitsuNimi):
    return loitsuNimi.lower()

for i in range(0, kordusteArv):
    print(loits(loitsuNimi))