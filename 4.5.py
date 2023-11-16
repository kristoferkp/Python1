from tkinter import *
import requests
from PIL import ImageTk, Image

# Ma ei viitsi teha seda, proovi ise teha ilma pildita
imageUrl = "https://rukman.ee/wp-content/uploads/2022/03/Picture3.jpg"

raam = Tk()
raam.title("Lill")
raam.geometry("600x600")

tahvel = Canvas(raam, width=600, height=400)
tahvel.pack()
tahvel.place(anchor="center", relx=0.5, rely=0.5)

imgData = requests.get(imageUrl).content

with open("image.jpg", "wb") as handler:
    handler.write(imgData)

img = ImageTk.PhotoImage(Image.open("image.jpg"))

label = Label(raam, image=img)
label.pack()

raam.mainloop()