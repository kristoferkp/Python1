# Prompt the user to enter the electricity price in cents per kilowatt-hour
hind = float(input("Sisesta elektrihind sentides kilovatt-tunni kohta: "))

# Define a function to convert the electricity price from cents per kilowatt-hour to euros per megawatt-hour
def elektrihind(hind):
    return hind * 10

# Print the original electricity price in cents per kilowatt-hour and the converted price in euros per megawatt-hour
print(str(hind) + " s/kWh on " + str(elektrihind(hind)) + " €/MWh")