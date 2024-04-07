import tkinter as tk
from transact import query

def Checkout(id):
    lName = tk.StringVar() #last name of purchaser
    lName.set("")

    fName = tk.StringVar() #first name of purchaser
    fName.set("")

    card = tk.StringVar() #card num of purchaser
    card.set("")

    items = query("getCart", id) #loads in everything YOU added to the cart in THIS SPECIFIC transaction

    root = tk.Tk()
    root.title("Purchase your meat.")
    
    total = 0
    for item in items: 
        l = tk.Label(root,text="{}, {} pounds".format(item[0][1], item[0][2]))
        l.pack()
        total+= item[1]

    totalCost = tk.Label(root, text=total)
    lnField = tk.Entry(root,textvariable=lName)
    fnField = tk.Entry(root,textvariable=fName)
    cField = tk.Entry(root,textvariable=card)

    totalCost.pack()
    lnField.pack()
    fnField.pack()
    cField.pack()


    root.mainloop()