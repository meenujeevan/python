from tkinter import *
import tkinter.messagebox as tkmb
root = Tk()
root.title('Home Bakery')

import re




def clear():
     
    # clear the content of text entry box
    nameentry.delete(0, END)
    emailentry.delete(0, END)
    passwordentry.delete(0, END)
    var.set('male')
    phoneentry.delete(0, END)
    

def getvals():

    check_counter=0
    warn = ""
    
    if namevalue.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if emailvalue.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if passwordvalue.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    
    if var.get() == "":
        warn = "gender can't be empty"
    else:
        check_counter += 1
        
    if phonevalue.get() == "":
        warn = "Phone no can't be empty"
    else:
        check_counter += 1
    
    
    
    
    password = passwordvalue.get()
    
    reg = r'^.*(?=.{5,10})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9!@£$%^&*()_+={}?:~\[\]]+$'

# compiling regex
    pattern = re.compile(reg)

# searching regex
    result = re.search(pattern, password)

# validating conditions
    if not result:
        warn ="password should contain at least one capital letter, one number and one special character. We also need the length of the password to be between 5 and 10"
         
    else:
        check_counter += 1   
    
    email = emailvalue.get()
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    pattern = re.compile(regex)
    res = re.fullmatch(pattern, email)

    if not res:
       warn ="please enter a valid Email"
    else:
       check_counter += 1
                

    
    
  
    if check_counter == 7:        
        try:
            print(f"{namevalue.get(), emailvalue.get(), passwordvalue.get(), var.get(), phonevalue.get()} ")
    
            with open("formdetls.txt", "a") as f:
                f.write(f"{namevalue.get(),emailvalue.get(),passwordvalue.get(),var.get(),phonevalue.get()}\n")
            
            tkmb.showinfo('confirmation', 'Registered successfully')
            nameentry.focus_set()
            clear()

        except Exception as ep:
            tkmb.showerror('', ep) 
    else:
        tkmb.showerror('Error', warn)
        
        
def clear1():
     
    # clear the content of text entry box
    
    email1entry.delete(0, END)
    password1entry.delete(0, END)
    
    
        
def getvals1():
    
    
        
    uname = emailvalue1.get()
    upwd = passwordvalue1.get()
    
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        with open('formdetls.txt') as f:
            lines = f.readlines()          
            for line in lines:   
                currentline = line.split(",")
                email=currentline[1].strip(" '")
                password=currentline[2].strip(" '")
                if (uname == email and upwd == password):
                    tkmb.showinfo('Login Status', 'Logged in Successfully!') 
                    email1entry.focus_set()
                    clear1()
                    break
                
            else:
                tkmb.showerror('Login Status', 'invalid username or password')
    else:
        tkmb.showerror('', warn)

        
        
        
        
root.geometry("844x544")        

Label(root, text="Welcome to Home Bakery", font="comicsansms 13 bold", pady=10).grid(row=0, column=2)
        


#Text for our form
name = Label(root, text="Name")
email = Label(root, text="Email")
password = Label(root, text="Password")
gender = Label(root, text="Gender")
phone = Label(root, text="Phone")



#Pack text for our form
name.grid(row=1, column=1, sticky='')
email.grid(row=2, column=1, sticky='')
password.grid(row=3, column=1, sticky='')
gender.grid(row=4, column=1, sticky='')
phone.grid(row=5, column=1, sticky='')

# Tkinter variable for storing entries
namevalue = StringVar()
emailvalue = StringVar()
passwordvalue = StringVar()
phonevalue = StringVar()
var = StringVar()
var.set('male')

#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
emailentry = Entry(root, textvariable=emailvalue)
passwordentry = Entry(root, textvariable=passwordvalue)
male = Radiobutton(root,text='Male',variable=var,value='male')
female = Radiobutton(root,text='Female',variable=var,value='female')

phoneentry = Entry(root, textvariable=phonevalue)

# Packing the Entries
nameentry.grid(row=1, column=2, sticky='', columnspan=2)
emailentry.grid(row=2, column=2, sticky='', columnspan=2)
passwordentry.grid(row=3, column=2, sticky='', columnspan=2)
male.grid(row=4, column=2, sticky='nsew', columnspan=2)
female.grid(row=4, column=3, sticky='nsew', columnspan=2)
phoneentry.grid(row=5, column=2, sticky='', columnspan=2)



#Button & packing it and assigning it a command
Button(text="Register",width=7, command=getvals).grid(row=6, column=2)

Label(root, text="Please Login here if you have already registered", font="comicsansms 10", pady=10).grid(row=7, column=2)


#loginform

Label(root, text="login Form", font="comicsansms 13 bold", pady=10).grid(row=8, column=2)

#Text for our form

UsernameorEmail = Label(root, text="Email")
Password = Label(root, text="Password")


UsernameorEmail.grid(row=9, column=1)
Password.grid(row=10, column=1)


emailvalue1 = StringVar()
passwordvalue1 = StringVar()

email1entry = Entry(root, textvariable=emailvalue1)
password1entry = Entry(root, textvariable=passwordvalue1)


email1entry.grid(row=9, column=2)
password1entry.grid(row=10, column=2)

#Button & packing it and assigning it a command
Button(text="Submit", command=getvals1).grid(row=11, column=2)

def forgotpass():
    uname = emailvalue1.get()
    check_counter=0
    if uname == "":
       warn = "please enter your emailid"
    else:
        check_counter += 1
    
    if check_counter == 1:
        with open('formdetls.txt') as f:
            lines = f.readlines()          
            for line in lines:   
                currentline = line.split(",")
                email=currentline[1].strip(" '")
                password=currentline[2].strip(" '")
                if (uname == email):
                    tkmb.showinfo('Your password is', password) 
                    password1entry.focus_set()
                    
                    break
                
            else:
                tkmb.showerror('Email not found', 'Please register your details first')
    else:
        tkmb.showerror('', warn)

Button(text="Forgot Password", command=forgotpass).grid(row=12, column=2)


root.mainloop()
