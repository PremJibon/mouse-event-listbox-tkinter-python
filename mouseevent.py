from tkinter import *

def doSomething(event):
    print("DO"+ str(event.x))

window = Tk()

window.bind("<Button-1>",doSomething) # left mouse button
window.bind("<Button-2>",doSomething) # do SOmething
window.bind("<Button-3>",doSomething) 
window.bind("<Leave>",doSomething)
window.bind("<Enter>",doSomething)
window.bind("<Motion>",doSomething)

window.mainloop()