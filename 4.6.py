from tkinter import *

raam = Tk()
raam.title("Emotikon")
raam.geometry("600x600")

tahvel = Canvas(raam, width=600, height=600)
tahvel.pack()

# Create a yellow circle for the face of the emoji
tahvel.create_oval(100, 100, 500, 500, fill="yellow")

# Create two smaller black circles for the eyes of the emoji
tahvel.create_oval(200, 200, 250, 250, fill="black")
tahvel.create_oval(350, 200, 400, 250, fill="black")

# Create an arc for the smile of the emoji
tahvel.create_arc(200, 250, 400, 450, start=0, extent=-180, fill="black")

raam.mainloop()