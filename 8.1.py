# Importing the ceil function from the math module
from math import ceil

# Function to calculate the investment amount
def invest(makse):
    """
    Calculate the investment amount by subtracting the integer part of the given payment.

    Parameters:
    makse (float): The payment amount.

    Returns:
    float: The investment amount.
    """
    return round(float(ceil(float(makse)) - float(makse)), 2)

# Prompting the user to enter the file name
failiNimi = input("Sisesta faili nimi: ")

# Opening the file in read mode
fail = open(failiNimi, "r", encoding="UTF-8")

maksed = []
# Reading each line from the file and appending it to the maksed list
for i in fail:
    maksed.append(i.strip())

fail.close()

investeering = 0

# Iterating over each payment in the maksed list
for makse in maksed:
    # Calculating the investment amount for each payment
    inv = invest(makse)
    
    # Checking if the investment amount is zero
    if inv == 0:
        print("Investeeringut ei tehta")
    
    # Printing the investment amount
    print(str(inv))
    
    # Adding the investment amount to the total investeering
    investeering += round(inv, 2)

# Rounding the total investeering to 2 decimal places
investeering = round(investeering, 2)

# Printing the total investeering amount
print("Investeeringute kogusumma: " + str(investeering) + " eurot.")