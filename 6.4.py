# This function counts the number of vowels (täishäälikud) in a given word.
def täishäälikud(sona):
    return sona.count("a") + sona.count("e") + sona.count("i") + sona.count("o")  + sona.count("u")  + sona.count("ä")  + sona.count("ü")  + sona.count("ö")  + sona.count("õ")

# Prompt the user to enter a word.
sona = input("Sisesta sõna: ")

# Call the täishäälikud function to count the vowels in the word and print the result.
print("Sõnas", sona, "on täishäälikuid", str(täishäälikud(sona)))