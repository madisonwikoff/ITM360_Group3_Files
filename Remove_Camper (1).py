from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import date

def master():
    root = Tk()
    root.title('Camper Registration')
    root.geometry("750x250")
    
    heading = Label(root, text = "Remove Camper", font = ("Verdana", 20), padx = 20, pady = 30)
    heading.pack()
    
    applicationFrame = LabelFrame(root, text = "Camper Information", padx = 5, pady = 5)
    applicationFrame.pack(side = LEFT, padx = 10, pady = 10)
    
    searchDatabase = LabelFrame(root, text = "Search Camper Information", padx = 5, pady = 5)
    searchDatabase.pack(side = LEFT, padx = 10, pady = 10)
    
    #Application Frame Inputs
    camperID = Entry(applicationFrame, width=30)
    camperID.grid(row=0, column=1, padx=20, pady=(10, 0))
    camperID_label = Label(applicationFrame, text="Camper ID", font = ("Verdana", 12)).grid(row=0, column=0, pady=(10, 0), sticky = W)
    


    remove_btn = Button(applicationFrame, text="Remove Records", font = ("Verdana", 12))
    remove_btn.grid(row=2, column=0, columnspan = 2,  pady=10, padx=10)
    
    
    
    #Search Frame Inputs 
    Label(searchDatabase, text="Search by").grid(row = 0, column = 0)
    searchQualities = ['first_name', 'last_name', 'mobile', 'address', 'city',
                 'state', 'zipcode', 'sex', 'age', 'payment_status', 'payment_date']
    
    searchQualitiesWidth = len(max(searchQualities, key=len))
    
    clicked3 = StringVar()
    clicked3.set(searchQualities[0])
    
    search_drop = OptionMenu(searchDatabase, clicked3, *searchQualities)
    search_drop.config(width=searchQualitiesWidth)
    search_drop.grid(row = 0, column = 0)
    
    search_entry = Entry(searchDatabase, width=30)
    search_entry.grid(row = 0, column = 1)
    
    Button(searchDatabase, text = "Search").grid(row = 0, column= 3)

    
 
    
    
    
    
    root.mainloop()

    
    
    
    
    
    
    
master()

    
    
    
    
    
    