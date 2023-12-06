# Prompt the user to enter the name of the file
failiNimi = input("Sisesta faili nimi: ")

# Open the file in read mode with UTF-8 encoding
fail = open(failiNimi, "r", encoding="UTF-8")

# Read the contents of the file and convert it to a string
sisu = str(fail.read())

# Close the file
fail.close()

# Replace all newline characters with a space
sisu = sisu.replace('\n', ' ')

# Prompt the user to enter the name of the new file
uusFailiNimi = input("Sisesta uue faili nimi: ")

# Open the new file in write mode with UTF-8 encoding
uusFail = open(uusFailiNimi, "w", encoding="UTF-8")

# Write the modified content to the new file
uusFail.write(sisu)

# Close the new file
uusFail.close()