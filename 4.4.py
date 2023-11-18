import tkinter

raam = tkinter.Tk()
raam.title("Auto")
raam.geometry("600x600")

tahvel = tkinter.Canvas(raam, width = 600, height = 600)
tahvel.pack()

tahvel.create_polygon(200, 100, 150, 150, 150, 225, 400, 225, 400, 100, fill="blue")
tahvel.create_rectangle(275, 125, 200, 175, fill="lightblue")
tahvel.create_rectangle(375, 125, 300, 175, fill="lightblue")
tahvel.create_oval(175, 200, 250, 275, fill="black")
tahvel.create_oval(300, 200, 375, 275, fill="black")

raam.mainloop()