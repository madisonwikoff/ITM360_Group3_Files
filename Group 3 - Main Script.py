from tkinter import *
import os
from tkinter import messagebox

PATH = r"C:\ACADEMICS\2021-2022 SPRING\ITM 360\TERM PROJECT\SCRIPTS"
os.chdir(PATH)
password_file = 'passwords.txt'

verified = False

def remember(verified):
    if verified == False:
        pass
    if verified == True:
        home.withdraw()
        options()

def addCamper():
    opt.withdraw()
    add = Tk()
    add.title('Camper Registration')
    add.geometry("850x600")
    
    heading = Label(add, text = "Add Camper", font = ("Verdana", 20), padx = 20, pady = 30)
    heading.pack()
    
    applicationFrame = LabelFrame(add, text = "Camper Information", padx = 5, pady = 5)
    applicationFrame.pack(side = LEFT, padx = 10, pady = 10)
    
    searchDatabase = LabelFrame(add, text = "Search Camper Information", padx = 5, pady = 5)
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

    submit_btn = Button(applicationFrame, text="Save Records", font = ("Verdana", 12))
    submit_btn.grid(row=11, column=0, columnspan = 2,  pady=10, padx=10)
    
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
    
    add.mainloop()

def removeCamper():
    opt.withdraw()
    remove = Tk()
    remove.title('Camper Registration')
    remove.geometry("750x250")
    
    heading = Label(remove, text = "Remove Camper", font = ("Verdana", 20), padx = 20, pady = 30)
    heading.pack()
    
    applicationFrame = LabelFrame(remove, text = "Camper Information", padx = 5, pady = 5)
    applicationFrame.pack(side = LEFT, padx = 10, pady = 10)
    
    searchDatabase = LabelFrame(remove, text = "Search Camper Information", padx = 5, pady = 5)
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
    
    remove.mainloop()

def updateCamper():
    opt.withdraw()
    edit = Tk()
    edit.title('Camper Registration')
    edit.geometry("850x600")
    
    heading = Label(edit, text = "Update Camper Information", font = ("Verdana", 20), padx = 20, pady = 30)
    heading.pack()
    
    applicationFrame = LabelFrame(edit, text = "Camper Information", padx = 5, pady = 5)
    applicationFrame.pack(side = LEFT, padx = 10, pady = 10)
    
    searchDatabase = LabelFrame(edit, text = "Search Camper Information", padx = 5, pady = 5)
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

    edit.mainloop()

def options():
    global opt
    home.withdraw()
    opt = Tk()
    opt.title("Gila Breath Camp")
    opt.geometry("800x500")
    
    heading = Label(opt, text = "Options", font = ("Verdana", 28), padx = 30, pady = 30)
    heading.pack()
    
    register = Button(opt, text = "       Add New Camper       ", font = ("Verdana", 12), padx = 20, pady = 10, command = addCamper)
    register.pack()
    spacer1 = Label(opt, text = "", padx = 20, pady = 10)
    spacer1.pack()
    
    edit = Button(opt, text = "  Edit Camper Information  ", font = ("Verdana", 12), padx = 20, pady = 10, command = updateCamper)
    edit.pack()
    spacer2 = Label(opt, text = "", padx = 20, pady = 10)
    spacer2.pack()
    
    remove = Button(opt, text = "Remove Camper from System", font = ("Verdana", 12), padx = 10, pady = 10, command = removeCamper)
    remove.pack()
    
    opt.mainloop()

def register_user():
 
    # get username and password
    username_info = username.get()
    password_info = password.get()
 
    # Open file
    file = open(password_file, "a")
 
    # write username and password information
    file.write(username_info + "\t")
    file.write(password_info + "\n")
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    # sucessful registration message
    
    messagebox.showinfo("Success!",
                        "You registered successfully!")
    reg.withdraw()

def login_verification():
    global verified
    
    username_verify = username_entry_login.get()
    password_verify = password_entry_login.get()
    
    users = {}
    if os.path.exists(password_file):
        with open(password_file, "r") as f:
            for line in f:
                user = line.split('\t')[0]
                pswd = line.split('\t')[1].strip()
                users[user] = pswd
            print(users)
            print(users.keys())
            
            if username_verify in users.keys():
                if users[username_verify] == password_verify:
                    verified = True
                    log.withdraw()
                    remember(verified)
                else:
                    messagebox.showerror('Warning!',
                                 "Your Username and Password do not match. \nPlease try again")
            else:
                messagebox.showerror('Error!',
                             "User not find.")
        f.close()
    else:
        messagebox.showerror('Error!',
                             "Please register first!")
        log.withdraw()

def registration():
    global username
    global password
    global username_entry
    global password_entry
    global reg
    global name_entry_login
    
    
    reg = Toplevel(home)
    reg.title("Register")
    reg.geometry("300x350")

    # text varaibles
    username = StringVar()
    password = StringVar()

    label_1 = Label(reg, text = "Employee Registration ", font = ("Calibri", 14), padx = 15, pady = 20)
    label_1.pack()
    
    # Create a Frame
    frame = LabelFrame(reg, text = "Please enter details below", padx = 5, pady = 5)
    frame.pack(padx = 10, pady = 10)

    name_entry_login = Entry(frame, width=20)
    name_entry_login.grid(row=0, column=1, sticky=W)
    name_label = Label(frame, text="Name * ", font=("Calibri", 12)).grid(row=0, sticky=W)

    jobtitle_entry_login = Entry(frame, width=20)
    jobtitle_entry_login.grid(row=1, column=1, sticky=W)
    job_label = Label(frame, text="Job Title * ", font=("Calibri", 12)).grid(row=1, sticky=W)
    
    # username label
    user_label  = Label(frame, text='Username * ', font = ("Calibri", 12)).grid(row=2, sticky=W)
 
    # username entry
    username_entry = Entry(frame, textvariable=username, width = 20)
    username_entry.grid(row = 2, column =1, sticky = W)
   
    # password label
    password_lable = Label(frame, text="Password * ", font = ("Calibri", 12)).grid(row=3, sticky=W)
     
    # password entry
    password_entry = Entry(frame, textvariable=password, width = 20, show='*')
    password_entry.grid(row=3, column =1, sticky = W)

    
    Label(reg, text="").pack()
    
    # register button
    Button(reg, text="Confirm", width=10, height=1, command= register_user).pack()
    
def login():
    global log
    
    log = Toplevel(home)
    log.title("Log In")
    log.geometry("300x250")


    global password_entry_login
    global username_entry_login
    global jobtitle_entry_login
    
    # text varaibles
    username_verify = StringVar()
    password_verify = StringVar()
  
    label_1 = Label(log, text = "Log In ", font = ("Calibri", 14), padx = 15, pady = 20)
    label_1.pack()
    
    # Create a Frame
    frame = LabelFrame(log, text = "Please enter your crendentials below", padx = 5, pady = 5)
    frame.pack(padx = 10, pady = 10)
    
    # username label
    user_label  = Label(frame, text='Username * ', font = ("Calibri", 12)).grid(row=0, sticky=W)
 
    # username entry
    username_entry_login = Entry(frame, width = 20, textvariable = username_verify)
    username_entry_login.grid(row = 0, column =1, sticky = W)
   
    # password label
    password_label = Label(frame, text="Password * ", font = ("Calibri", 12)).grid(row=1, sticky=W)
     
    # password entry
    password_entry_login = Entry(frame, width = 20, show='*', textvariable = password_verify)
    password_entry_login.grid(row=1, column =1, sticky = W)

    
    Label(log, text="").pack()

    
    # register button
    Button(log, text="Confirm", width=10, height=1, command=login_verification).pack()

def homepage():
    global home
    
    home = Tk()
    home.geometry("300x250")
    home.title("Gila Breath Camp - Employee Login")

    # Create a Form Label
    label_1 = Label(home, text = "Welcome to Gila Breath Camp ", font = ("Calibri", 16), padx = 20, pady = 30)
    label_1.pack()

    # Create a Frame
    frame = LabelFrame(home, text = "Employee Login", padx = 5, pady = 5)
    frame.pack(padx = 10, pady = 10)

    # create Login Button 
    Button(frame, text="Login", height="2", width="30", command = login).pack(padx = 5, pady = 8) 
 
    # create a register button
    Button(frame, text="Register", height="2", width="30", command = registration).pack(padx = 5, pady = 8)

    home.mainloop()

homepage()