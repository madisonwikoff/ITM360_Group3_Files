from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import date

def master():
    root = Tk()
    root.title('Camper Registration')
    root.geometry("850x600")
    
    heading = Label(root, text = "Update Camper Information", font = ("Verdana", 20), padx = 20, pady = 30)
    heading.pack()
    
    applicationFrame = LabelFrame(root, text = "Camper Information", padx = 5, pady = 5)
    applicationFrame.pack(side = LEFT, padx = 10, pady = 10)
    
    searchDatabase = LabelFrame(root, text = "Search Camper Information", padx = 5, pady = 5)
    searchDatabase.pack(side = LEFT, padx = 10, pady = 10)
    searchDatabase.config(pady = 200)
    
    #Application Frame Inputs
    f_name = Entry(applicationFrame, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    f_name_label = Label(applicationFrame, text="First Name", font = ("Verdana", 12)).grid(row=0, column=0, pady=(10, 0), sticky = W)
    
    l_name = Entry(applicationFrame, width=30)
    l_name.grid(row=1, column=1, padx=20, pady=(10, 0))
    l_name_label = Label(applicationFrame, text="Last Name", font = ("Verdana", 12)).grid(row=1, column=0, pady=(10, 0), sticky = W)
    
    mobile = Entry(applicationFrame, width=30)
    mobile.grid(row=2, column=1, padx=20, pady=(10, 0))
    mobile_label = Label(applicationFrame, text="Mobile Number", font = ("Verdana", 12)).grid(row=2, column=0, pady=(10, 0), sticky = W)
    
    address = Entry(applicationFrame, width=30)
    address.grid(row=3, column=1, padx=20, pady=(10, 0))
    address_label = Label(applicationFrame, text="Home Address", font = ("Verdana", 12)).grid(row=3, column=0, pady=(10, 0), sticky = W)
    
    city = Entry(applicationFrame, width=30)
    city.grid(row=4, column=1, padx=20, pady=(10, 0))
    city_label = Label(applicationFrame, text="City", font = ("Verdana", 12)).grid(row=4, column=0, pady=(10, 0), sticky = W)
    
    state = Entry(applicationFrame, width=30)
    state.grid(row=5, column=1, padx=20, pady=(10, 0))
    state_label = Label(applicationFrame, text="State", font = ("Verdana", 12)).grid(row=5, column=0, pady=(10, 0), sticky = W)
    
    zipcode = Entry(applicationFrame, width=30)
    zipcode.grid(row=6, column=1, padx=20, pady=(10, 0))
    zipcode_label = Label(applicationFrame, text="Zip Code", font = ("Verdana", 12)).grid(row=6, column=0, pady=(10, 0), sticky = W)
    
    Lsex = ['Male', 'Female']
    oMenuWidth = len(max(Lsex, key=len))
    clicked = StringVar()
    clicked.set(Lsex[0])
    camperSex = OptionMenu(applicationFrame, clicked, *Lsex)
    camperSex.config(width=oMenuWidth)
    camperSex.grid(row = 7, column = 1)
    camperSex_label = Label(applicationFrame, text="Sex", font = ("Verdana", 12)).grid(row=7, column=0, pady=(10, 0), sticky = W)

    age = Entry(applicationFrame, width=30)
    age.grid(row=8, column=1, padx=20, pady=(10, 0))
    age_label = Label(applicationFrame, text="Age", font = ("Verdana", 12)).grid(row=8, column=0, pady=(10, 0), sticky = W)
    
    LpaymentStatus = ['Paid', 'Pending']
    oMenuWidth = len(max(LpaymentStatus, key=len))
    clicked2 = StringVar()
    clicked2.set(LpaymentStatus[0])
    paymentStatus = OptionMenu(applicationFrame, clicked2, *LpaymentStatus)
    paymentStatus.config(width=oMenuWidth)
    paymentStatus.grid(row = 9, column = 1)
    paymentStatus_label = Label(applicationFrame, text="Payment Status", font = ("Verdana", 12)).grid(row=9, column=0, pady=(10, 0), sticky = W)

    payment_date = DateEntry(applicationFrame,width=30,bg="purple",fg="white", 
                             year = date.today().year)
    payment_date.grid(row=10, column=1)
    paymentDate_label = Label(applicationFrame, text="Payment Date", font = ("Verdana", 12)).grid(row=10, column=0, pady=(10, 0), sticky = W)



    update_btn = Button(applicationFrame, text="Update Records", font = ("Verdana", 12))
    update_btn.grid(row=11, column=0, columnspan = 2,  pady=10, padx=10)
    
    
    
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

    
    
    
    
    
    