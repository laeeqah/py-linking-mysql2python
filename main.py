from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                               host = "localhost", database = "hospital",
                               auth_plugin = "mysql_native_password")

mycursor = mydb.cursor()

def  verify():
    user = name_entry.get()
    passs = pass_word_entry.get()
    sql = "select * from Login where username = %s and password = %s"
    mycursor.execute(sql, [(user), (passs)])
    results = mycursor.fetchall() #fetches all the data(shortcut)
    if results:
        window.withdraw()

        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    messagebox.showinfo("Successful","You have succesfully logged in") #If the log in is successful a messagebox will appear
    # This is the second interface
    window2 = Tk()
    window2.title("Logged in")
    window2.geometry("450x450")
    infolb = Label(window2, text = "")
    infolb.place(x = 20, y = 20)
    countlb = Label(window2, text = "")
    countlb.place(x = 80, y = 100)
    mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                               host = "localhost", database = "hospital",
                               auth_plugin = "mysql_native_password")

    mycursor = mydb.cursor()

    secsql = mycursor.execute("select * from Login ") #This will make the data appear on the next interface
    for i in mycursor:
        print(i)
        mydata = str(i)
        infolb['text'] += "\n" + mydata


    secsql = mycursor.execute("select count(*) from Login ")
    for i in mycursor:
        print(i)



def failed(): #If it fails to log in the error will appear and clear the entries
    messagebox.showerror("Error", "Username or Password is incorrect")
    pass_word_entry.delete(0,END)
    name_entry.delete(0,END)

# This is the first interface
window = Tk()
window.title("Login Page")
window.geometry("450x450")

# The labels
name = Label(window, text = "Please enter username")
name.place(x = 40,y = 20)

pass_word = Label(window, text = "Please enter password")
pass_word.place(x = 40, y = 60)

# The Entries
name_entry = Entry(window)
name_entry.place(x = 200, y = 20)

pass_word_entry = Entry(window)
pass_word_entry.place(x = 200, y = 60)

# The Buttons
login_btn = Button(window, text = "Login", command = verify)
login_btn.place(x = 150, y = 150, width = "55")
login_btn.configure(background = "pink")

# register_user = Button(window, text = "Register")
# register_user.place(x = 250, y = 150)
window.mainloop()


