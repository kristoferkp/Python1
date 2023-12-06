# Import the datetime module
from datetime import datetime

# Prompt the user to enter a special day and a date
tahtpaev = input("Sisesta tähtpäev: ")
kuupaev = input("Sisesta kuupäev: ")

# Convert the entered date to a datetime object and extract the weekday
paev = datetime.strptime(kuupaev, "%d.%m.%Y")
paev = paev.isoweekday()

# Define a dictionary to map weekdays to their corresponding names in Estonian
paevad = {
    "1": "esmaspäev",
    "2": "teisipäev",
    "3": "kolmapäev",
    "4": "neljapäev",
    "5": "reede",
    "6": "laupäev",
    "7": "pühapäev"
}

# Print the name of the weekday based on the entered date
print(paevad[str(paev)])

# Open the file "tähtpäevad.txt" in append mode and write the entered special day, date, and weekday
fail = open("tähtpäevad.txt", "a", encoding="UTF-8")
fail.write("Tähtpäev: " + tahtpaev + "\n")
fail.write("Kuupäev: " + kuupaev + "\n")
fail.write("Nädalapäev on " + paevad[str(paev)] + ".")

# Close the file
fail.close()