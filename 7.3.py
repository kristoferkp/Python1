# Importing the necessary function from the easygui module
from easygui import *

# Prompt the user to enter a question
kusimus = enterbox("Tere! Mida sooviksite küsida?")

# Check if the question is "Mis on 9 + 10?"
if kusimus == "Mis on 9 + 10?":
    # Display the answer if the question is correct
    msgbox("21")

# Check if the question is "Milline on tänane ilm?"
if kusimus == "Milline on tänane ilm?":
    # Display a suggestion to look out of the window for the answer
    msgbox("Ma ei tea, vaata aknast välja.")

# If the question is neither of the above, display a default message
else:
    msgbox("Ei oska öelda, proovi uuesti.")