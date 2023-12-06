# Prompt the user to enter the name of the file
failiNimi = input("Sisesta faili nimi: ")

# Open the file with the given name and UTF-8 encoding
fail = open(failiNimi, encoding="UTF-8")

# Create an empty list to store the names
nimed = []

# Read each line from the file and append it to the list after removing any leading or trailing whitespace
for rida in fail:
    nimed.append(rida.strip())

# Close the file
fail.close()

# Prompt the user to enter the starting letter of the names
algusTaht = input("Sisesta nime algustäht: ")

# Prompt the user to enter the minimum length of the names
pikkus = int(input("Sisesta nime minimaalne pikkus: "))

# Create an empty list to store the suitable names
sobilikudNimed = []

# Iterate over each name in the list
for nimi in nimed:
    # Check if the name starts with the given letter (ignoring case) and has a length greater than or equal to the minimum length
    if nimi.startswith(algusTaht.upper()) and len(nimi) >= pikkus:
        # If the conditions are met, add the name to the suitable names list
        sobilikudNimed.append(nimi)

# Print the suitable names
print("Sobilikud nimed on: \n")
for nimi in sobilikudNimed:
    print(nimi)

# Define a function named "nimeotsing" that takes three parameters but doesn't do anything
# This function is not used in the code, but it is included to meet the requirements of the website lahendus.ut.ee
def nimeotsing(see, eiTee, sittagi):
    return sobilikudNimed

# Call the nimeotsing function with some arbitrary arguments (not relevant to the code)
nimeotsing(100, 69, 420)