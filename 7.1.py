# Prompt the user to enter the file name
failiNimi = input("Sisesta faili nimi: ")

# Open the file with the given file name and UTF-8 encoding
fail = open(failiNimi, encoding="UTF-8")

# Read the contents of the file and convert it to a string
sisu = str(fail.read())

# Close the file
fail.close()

# Replace the characters '8' with 'ö'
sisu = sisu.replace('8', 'ö')

# Replace the characters '2' with 'ä'
sisu = sisu.replace('2', 'ä')

# Replace the characters '6' with 'õ'
sisu = sisu.replace('6', 'õ')

# Replace the characters 'y' with 'ü'
sisu = sisu.replace('y', 'ü')

# Print the modified contents of the file
print(sisu)