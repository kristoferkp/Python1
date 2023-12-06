# Ask the user for the name of the file
failiNimi = input("Sisesta faili nimi: ")

# Open the file in read mode with UTF-8 encoding
fail = open(failiNimi, "r", encoding="UTF-8")

# Initialize an empty list to store the data from the file
andmed = []

# Loop through each line in the file
for i in fail:
    # Remove any leading or trailing whitespace from the line and append it to the list
    andmed.append(i.strip())
    
# Close the file
fail.close()

# Define a function to determine the type based on the value
def tüüp(arv):
    # If the value is greater than 25000, it's type FFP1
    if arv > 25000:
        return "FFP1"
    # If the value is greater than 5000, it's type FFP2
    elif arv > 5000:
        return "FFP2"
    # If the value is less than or equal to 5000, it's type FFP3
    elif arv <= 5000:
        return "FFP3"

# Initialize a counter for the total number of FFP2 and FFP3 masks
kokku = 0

# Loop through the data
for i in andmed:
    # If the type of the mask is FFP3 or FFP2, increment the counter
    if tüüp(int(i)) == "FFP3" or tüüp(int(i)) == "FFP2":
        kokku += 1

# Print the total number of FFP2 and FFP3 masks
print("FFP2 ja FFP3 tüüpi maske oli kokku " + str(kokku) + ".")