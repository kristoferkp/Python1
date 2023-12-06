# Prompt the user for the number of times they want to use the spell
kordusteArv = int(input("Mitu korda soovite loitsu kasutada? "))

# Prompt the user for the spell name
loitsuNimi = input("Sisesta loits: ")
    
# Define a function to convert the spell name to lowercase
def loits(loitsuNimi):
    return loitsuNimi.lower()

# Iterate over the range of kordusteArv and print the lowercase spell name
for i in range(0, kordusteArv):
    print(loits(loitsuNimi))