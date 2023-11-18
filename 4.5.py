from tkinter import *
import math

raam = Tk()
raam.title("Lill")
raam.geometry("600x600")

tahvel = Canvas(raam, width=600, height=600)
tahvel.pack()

center_x, center_y = 300, 300  # center point
radius = 100  # radius of rotation
oval_width, oval_height = 200, 200  # size of ovals

for i in range(12):
    angle = 2 * math.pi * i / 12  # angle of each oval
    top_left_x = center_x + radius * math.cos(angle) - oval_width / 2
    top_left_y = center_y + radius * math.sin(angle) - oval_height / 2
    bottom_right_x = top_left_x + oval_width
    bottom_right_y = top_left_y + oval_height
    tahvel.create_oval(top_left_x, top_left_y, bottom_right_x, bottom_right_y, fill="blue")

tahvel.create_oval(200, 200, 400, 400, fill="#FFFF00")


raam.mainloop()