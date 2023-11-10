from tkinter import *
import requests
from PIL import ImageTk, Image

imageUrl="https://emojiisland.com/cdn/shop/products/Emoji_Icon_-_Smiling_large.png?v=1571606089"

raam = Tk()
raam.title("Emotikon")
raam.geometry("700x500")

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