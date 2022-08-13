import os
import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox

w = tk.Tk()

def balanse():
    id = e1.get()
    balance = e2.get()
    if e1.get() != '' and e2.get() != '':
        url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={}&balance={}".format(id, balance)
        res = requests.get(url)
        url2 = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={}".format(id)
        output = requests.get(url2)
        json = output.json()
    
        for i in json:
            id1 = i["id"]
            name = i["name"]
            surname = i["surname"]
            email = i["email"]
            school_group = i["school_group"]
            status = i["status"]
            balance1 = i["balance"]
            if i["id"] is None:
                messagebox.showerror('Error', 'No User')
            else:
                l3.config(text="Id: {}\nName: {}\nSurname: {}\nEmail: {}\nGroup: {}\nStatus: {}\nBalance: {}".format(id1, name, surname, email, school_group, status, balance1))


f1 = tk.Frame(master = w, width = 600,height = 600,bg = "violet")
f1.pack(fill = tk.BOTH,expand = True)

l1 = tk.Label(master= f1,text = "Please enter id:",bg = "violet")
l1.grid(row = 0,column = 1,padx = 10,pady = 10)

e1 = tk.Entry(master = f1,width = 10)
e1.grid(row = 0,column = 2,padx = 10,pady = 10)

l2 = tk.Label(master= f1,text = "Enter balanse:",bg = "violet")
l2.grid(row = 1,column = 1,padx = 10,pady = 10)

e2 = tk.Entry(master=f1, width = 10)
e2.grid(row = 1,column = 2,padx = 10,pady = 10)

f2 = tk.Frame(master = w, width = 600,height = 600,bg = "pink")
f2.pack(fill = tk.BOTH,expand = True)

l3 = tk.Label(master= f2,text = "w",bg = "pink")
l3.grid(row = 0,column = 1,padx = 10,pady = 10)

f3 = tk.Frame(master = w, width = 600,height = 600,bg = "violet")
f3.pack(fill = tk.BOTH,expand = True)

b1 = tk.Button(master = f3,text = "Change balanse",command = balanse)
b1.pack(fill = tk.BOTH,expand = True)


w.mainloop()