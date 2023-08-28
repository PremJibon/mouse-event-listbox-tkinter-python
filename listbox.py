from tkinter import *

def submit():
    print(listbox.get(listbox.curselection()))


def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
root = Tk()

listbox = Listbox(root,bg='#f7ffde',font=("Constantia",35),width=12)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(root)
entryBox.pack()

addButton = Button(root,text='Add',command=add)
addButton.pack()

submitButton = Button(root,text='submit',command=submit)
submitButton.pack()

deleteButton = Button(root,text='delete',command=delete)
deleteButton.pack()

root.mainloop()