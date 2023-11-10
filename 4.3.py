from tkinter import *

raam = Tk()
raam.title("Kuusk")

tahvel = Canvas(raam, width=600)
tahvel.pack()

tahvel.create_polygon(100, 100, 50, 150, 150, 150, fill="green")
tahvel.create_polygon(100, 150, 50, 200, 150, 200, fill="green")
tahvel.create_rectangle(85, 200, 115, 240, fill="brown")

raam.mainloop()