import tkinter as tk
from transact import query
import uuid


def Checkout(id):
    
    meatPairs = {}
    
    transNum = uuid.uuid4() #purchaseID
    def check(tot):
        last = lName.get()
        cardNum = card.get()

        query("purchase", [str(transNum),cardNum[len(cardNum)-4:],last,tot, meatPairs])

    lName = tk.StringVar() #last name of purchaser
    lName.set("")

    fName = tk.StringVar() #first name of purchaser
    fName.set("")

    card = tk.StringVar() #card num of purchaser
    card.set("")

    items = query("getCart", id) #loads in everything YOU added to the cart in THIS SPECIFIC transaction

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Purchase your meat.")
    
    total = 0
    for item in items: 
        l = tk.Label(root,text="{}, {} pounds".format(item[0][1], item[0][2]))
        l.grid(sticky="w") # align to the left
        total+= item[1]
        meatPairs[item[0][1]] = item[0][2]

    totalCost = tk.Label(root, text=f"Total: ${total:.2f}")
    totalCost.grid(sticky='w')

    # Labels for the entry fields
    lnLabel = tk.Label(root, text="Last Name:")
    fnLabel = tk.Label(root, text="First Name:")
    cLabel = tk.Label(root, text="Card Number:")

    lnLabel.grid(row=len(items) + 1, column=0, sticky='e')
    fnLabel.grid(row=len(items) + 2, column=0, sticky='e')
    cLabel.grid(row=len(items) + 3, column=0, sticky='e')

    # Entry fields
    lnField = tk.Entry(root, textvariable=lName)
    fnField = tk.Entry(root, textvariable=fName)
    cField = tk.Entry(root, textvariable=card)

    lnField.grid(row=len(items) + 1, column=1)
    fnField.grid(row=len(items) + 2, column=1)
    cField.grid(row=len(items) + 3, column=1)

    # Checkout button 
    checkoutButton = tk.Button(root, text="Checkout", command= lambda t = total :check(t))
    checkoutButton.grid(row=len(items) + 4, column=0, columnspan=2, pady=10)
    # add functionality

    root.mainloop()