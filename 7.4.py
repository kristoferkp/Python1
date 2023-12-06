# Import the ceil function from the math module
from math import ceil

# Define a function named tordi_kogus that takes two parameters: kogus and inimesteArv
# This function calculates the amount of cake needed based on the quantity and number of people
def tordi_kogus(kogus, inimesteArv):
    return ceil(kogus * inimesteArv / 1000)

# Prompt the user to enter the file name
failiNimi = input("Sisesta faili nimi: ")

# Open the file in read mode with UTF-8 encoding
fail = open(failiNimi, "r", encoding="UTF-8")

# Read the contents of the file and convert it to a string
sisu = str(fail.read())

# Close the file
fail.close()

# Count the number of occurrences of the word "jah" in the file and convert it to an integer
inimesteArv = int(sisu.count("jah"))

# Print the number of people to consider when ordering the cake
print("Tordi tellimisel tuleb arvestada " + str(inimesteArv) + " inimesega.")

# Calculate and print the amount of regular cake needed based on the quantity 150 and the number of people
print("Tavalist torti on vaja " + str(tordi_kogus(150, inimesteArv)) + " kg.")

# Calculate and print the amount of cake with berry jelly topping needed based on the quantity 200 and the number of people
print("Marjaželee kattega torti on vaja " + str(tordi_kogus(200, inimesteArv)) + " kg.")