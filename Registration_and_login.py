from tkinter import *
import os
from tkinter import messagebox

PATH = "/Users/chrispollock/Desktop/ITM360/2/22"
os.chdir(PATH)
password_file = 'passwords.txt'


# Registration Screen
def register():

    global username
    global password
    global username_entry
    global password_entry
    global register_screen
    global name_entry_login
    
    
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("300x350")

    # text varaibles
    username = StringVar()
    password = StringVar()

    label_1 = Label(register_screen, text = "Employee Registration ", font = ("Calibri", 14), padx = 15, pady = 20)
    label_1.pack()
    
    # Create a Frame
    frame = LabelFrame(register_screen, text = "Please enter details below", padx = 5, pady = 5)
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

    
    Label(register_screen, text="").pack()
    
    # register button
    Button(register_screen, text="Confirm", width=10, height=1, command= register_user).pack()


# Register button
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
    register_screen.destroy()


# Login screen
def login():
    
    global login_screen
    
    login_screen = Toplevel(root)
    login_screen.title("Log In")
    login_screen.geometry("300x250")


    global password_entry_login
    global username_entry_login
    global jobtitle_entry_login
    
    # text varaibles
    username_verify = StringVar()
    password_verify = StringVar()
  
    label_1 = Label(login_screen, text = "Log In ", font = ("Calibri", 14), padx = 15, pady = 20)
    label_1.pack()
    
    # Create a Frame
    frame = LabelFrame(login_screen, text = "Please enter your crendentials below", padx = 5, pady = 5)
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

    
    Label(login_screen, text="").pack()

    
    # register button
    Button(login_screen, text="Confirm", width=10, height=1, command=login_verification).pack()


def login_verification():
    
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
                    messagebox.showinfo("Success!",
                                        'You have logged in to Gila Breath Camp.')
                    login_screen.destroy()
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
        login_screen.destroy()


def master_screen():

    global root 
    root = Tk()
    root.geometry("300x250")
    root.title("Gila Breath Camp - Employee Login")

    # Create a Form Label
    label_1 = Label(root, text = "Welcome to Gila Breath Camp ", font = ("Calibri", 16), padx = 20, pady = 30)
    label_1.pack()


    # Create a Frame
    frame = LabelFrame(root, text = "Employee Login", padx = 5, pady = 5)
    frame.pack(padx = 10, pady = 10)



    # create Login Button 
    Button(frame, text="Login", height="2", width="30", command = login).pack(padx = 5, pady = 8) 
 
 
    # create a register button
    Button(frame, text="Register", height="2", width="30", command = register).pack(padx = 5, pady = 8)

    root.mainloop() 


# Call the function
master_screen()



