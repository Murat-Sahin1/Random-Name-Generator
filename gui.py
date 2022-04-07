from tkinter import *

window = Tk()  # window instance
window.geometry("500x500")
window.title("Random Name Generator")

my_icon = PhotoImage(file='venv/Lib/assets/images/crow.png')
window.iconphoto(True, my_icon)
window.config(background="#36393e")

window.mainloop()


