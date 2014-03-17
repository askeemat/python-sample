from Tkinter import *

screen_width = 600
screen_height = 900


root = Tk()
root.geometry(str(screen_width) + "x" + str(screen_height))
upper_frame = Frame(root, height = 100)
upper_frame.pack(fill = BOTH, side = BOTTOM)


clear_button = Button(upper_frame, text = "clear")
clear_button.place()
clear_button.pack(fill = BOTH)

c0 = Canvas(root, width = 140, height = 140, bg = "white")
c0.pack(expand = True, fill = BOTH)

c0.create_rectangle(100, 100, 200, 250, outline="green")

root.mainloop()
