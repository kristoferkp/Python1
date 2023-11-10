from tkinter import *
import requests
from PIL import ImageTk, Image

imageUrl = "https://rukman.ee/wp-content/uploads/2022/03/Picture3.jpg"

raam = Tk()
raam.title("Lill")
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