# Prompt the user to enter the file name
failiNimi = input("Sisesta faili nimi: ")

# Open the file with the given file name and UTF-8 encoding
fail = open(failiNimi, encoding="UTF-8")

# Create an empty list to store the grades
hinded = []

# Read each line from the file and append the grades to the list
for rida in fail:
    hinded.append(int(rida.strip()))

# Close the file
fail.close()

# Define a function to calculate the average grade
def hinnete_keskmine(hinded):
    kokku = 0

    # Check if there are any grades below 3 (1 or 2)
    if hinded.count(1) > 0 or hinded.count(2) > 0:
        return -1
    else:
        # Calculate the sum of all grades
        for hinne in hinded:
            kokku += int(hinne)

        # Calculate the average grade and round it to 1 decimal place
        return round(kokku / len(hinded), 1)

# Check the average grade using the hinnete_keskmine function
if hinnete_keskmine(hinded) == -1:
    print("Õpilasel on mitterahuldavaid hindeid")
else:
    print("Hinnete keskmine on " + str(hinnete_keskmine(hinded)))