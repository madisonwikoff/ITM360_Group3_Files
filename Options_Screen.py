from tkinter import *

def options():
    root = Tk()
    root.title("Gila Breath Camp")
    root.geometry("800x500")
    
    heading = Label(root, text = "Options", font = ("Verdana", 28), padx = 30, pady = 30)
    heading.pack()
    
    register = Button(root, text = "       Add New Camper       ", font = ("Verdana", 12), padx = 20, pady = 10)
    register.pack()
    spacer1 = Label(root, text = "", padx = 20, pady = 10)
    spacer1.pack()
    
    edit = Button(root, text = "  Edit Camper Information  ", font = ("Verdana", 12), padx = 20, pady = 10)
    edit.pack()
    spacer2 = Label(root, text = "", padx = 20, pady = 10)
    spacer2.pack()
    
    remove = Button(root, text = "Remove Camper from System", font = ("Verdana", 12), padx = 10, pady = 10)
    remove.pack()
    
    root.mainloop()
    
options()