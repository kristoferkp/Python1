from easygui import *

kusimus = enterbox("Tere! Mida sooviksite küsida?")

if kusimus == "Mis on 9 + 10?":
    msgbox("21")
    
if kusimus == "Milline on tänane ilm?":
    msgbox("Ma ei tea, vaata aknast välja.")
    
else:
    msgbox("Ei oska öelda, proovi uuesti.")