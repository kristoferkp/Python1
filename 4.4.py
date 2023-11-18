from tkinter import *

raam = Tk()
raam.title("Auto")
raam.geometry("600x600")

tahvel = Canvas(raam, width = 600)
tahvel.pack()

tahvel.create_polygon(200, 100, 150, 150, 150, 225, 400, 225, 400, 100, fill="red")
tahvel.create_rectangle(275, 125, 200, 175, fill="blue")
tahvel.create_rectangle(375, 125, 300, 175, fill="blue")
tahvel.create_oval(200, 200, 250, 250, fill="black")
tahvel.create_oval(300, 200, 350, 250, fill="black")

raam.mainloop()