"""
This script reads two text files, 'alghinnad.txt' and 'hinnakordajad.txt',
which contain initial prices and price multipliers respectively.
It calculates the discounted price for each product based on the multiplier,
and then calculates the total cost of all products.

The script assumes that the text files are encoded in UTF-8.

Example usage:
python 5.6.py
"""

# Open the 'alghinnad.txt' file for reading
alghinnad = open("alghinnad.txt", encoding="UTF-8")

# Open the 'hinnakordajad.txt' file for reading
hinnakordajad = open("hinnakordajad.txt", encoding="UTF-8")

# Create empty lists to store the prices and multipliers
hinnad = []
kordajad = []

# Read each line in 'alghinnad.txt' and append it to the 'hinnad' list
for i in alghinnad:
    hinnad.append(i.strip())
alghinnad.close()

# Read each line in 'hinnakordajad.txt' and append it to the 'kordajad' list
for i in hinnakordajad:
    kordajad.append(i.strip())
hinnakordajad.close()

# Initialize a variable to store the total cost
kokku = 0

# Iterate over the prices and multipliers using enumerate
for index, hind in enumerate(hinnad):
    # Calculate the discounted price for each product
    kampaaniahind = float(hind) * float(kordajad[int(index)])
    
    # Print the product's index, initial price, and discounted price
    print(str(index + 1) + ". toote alghind: " + str(hind) + ", kampaaniahind: " + str(kampaaniahind))
    
    # Add the discounted price to the total cost
    kokku += kampaaniahind
    
# Print the total cost of all products
print("Toodete kogumaksumus on " + str(kokku))
alghinnad = open("alghinnad.txt", encoding = "UTF-8")
hinnakordajad = open("hinnakordajad.txt", encoding = "UTF-8")