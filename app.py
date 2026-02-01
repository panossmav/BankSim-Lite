from tkinter import *
import tkinter as tk 
from tkinter import messagebox
from basic_comms import *

root = tk.Tk()
root.title("Bank System Sim")

def create_customer_gui():
    new_customer = tk.Tk()
    new_customer.title("Create a new customer")
    
    tk.Label(new_customer, text='Name').pack()
    name_e = tk.Entry(new_customer)
    name_e.pack()

    tk.Label(new_customer, text='Date of Birth').pack()
    dob_e = tk.Entry(new_customer)
    dob_e.pack()

    tk.Label(new_customer, text='Phone Number').pack()
    phoneno_e = tk.Entry(new_customer)
    phoneno_e.pack()

    tk.Label(new_customer, text='Email').pack()
    email_e = tk.Entry(new_customer)
    email_e.pack()

    tk.Label(new_customer, text='Home Address').pack()
    homeaddr_e = tk.Entry(new_customer)
    homeaddr_e.pack()

    tk.Label(new_customer, text='VAT').pack()
    vat_e = tk.Entry(new_customer)
    vat_e.pack()

    tk.Label(new_customer, text='Citizen Of').pack()
    citizenof_e = tk.Entry(new_customer)
    citizenof_e.pack()

    tk.Label(new_customer, text='ID Number').pack()
    idnum_e = tk.Entry(new_customer)
    idnum_e.pack()
    
    def create_customer_bridge():
        name = name_e.get()
        dob = dob_e.get()
        phoneno = phoneno_e.get()
        email = email_e.get()
        homeaddr = homeaddr_e.get()
        vat = vat_e.get()
        citizenof = citizenof_e.get()
        idnum = idnum_e.get()
        id,status = create_customer(name,dob,phoneno,email,homeaddr,vat,citizenof,idnum)
        if status == True:
            tk.messagebox.showinfo(f"Customer {id} Created")
        else:
            tk.messagebox.showerror("Found")
    
    tk.Button(new_customer,text='Apply',command=create_customer_bridge).pack()



    new_customer.mainloop()

tk.Label(root,text='Welcome to the demo bank simulator!').pack()
tk.Button(root,text='Create Customer',command=create_customer_gui).pack()

root.mainloop()