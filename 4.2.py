from tkinter import *

raam = Tk()
raam.title("no")

tahvel = Canvas(raam, width=600)
tahvel.pack()

tahvel.create_rectangle(50, 100, 100, 200, fill="green")
tahvel.create_rectangle(100, 100, 200, 150, fill="yellow")
tahvel.create_rectangle(100, 150, 200, 200, fill="red")

raam.mainloop()
