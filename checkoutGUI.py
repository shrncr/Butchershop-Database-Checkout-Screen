import tkinter as tk
from transact import query
import uuid
from time import sleep

def Checkout(id):


    meatPairs = {}
    
    def on_field_select(entry):
        print(entry)
        selectedField = entry
    def add_text(let):
        field= root.focus_get()
        if field:
            field.insert(tk.END, let)
    def check(tot):
        transNum = uuid.uuid4() #purchaseID
        last = lnField.get()
        cardNum = cField.get()
        print(cardNum)
        print("Debug Info:", str(transNum), cardNum[len(cardNum)-4:], last, tot)  # Debug output
        query("purchase", [str(transNum),cardNum[len(cardNum)-4:],last,tot, meatPairs])
        
    # Clear all widgets
        for widget in root.winfo_children():
            widget.destroy()
       # Display success message
        success_message = tk.Label(root, text="Thank you!", font=("system", 40), fg="black")
        success_message.pack(pady=200)  # Centers the message in the window

        # Schedule window to close after 6000 milliseconds (6 seconds)
        root.after(6000, root.destroy)
        

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
    root.configure(background="white")
    root.attributes('-fullscreen',True)
    
    total = 0
    for item in items: 
        l = tk.Label(root,bg="white", font=("system",80), fg="black",text="{}, {} pounds".format(item[0][2], item[0][3]))
        l.grid(sticky="w") # align to the left
        total+= item[1]
        meatPairs[item[0][2]] = item[0][3]
        print(meatPairs)

    totalCost = tk.Label(root,bg="white", font=("system",100), fg="black", text=f"Total: ${total:.2f}")
    totalCost.grid(sticky='w')

    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    button_frame = tk.Frame(root, bg="white")
    button_frame.grid(row=len(items)+1, column=13, columnspan=8)
    for idx, char in enumerate(characters):
        b = tk.Button(button_frame, bg="white", font=("system", 20), fg="black", text=char, command=lambda l=char: add_text(l))
        b.grid(row=(idx//10), column=(idx%10))  # Arranged in a 10x5 grid

    # Labels for the entry fields
    lnLabel = tk.Label(root,bg="white", font=("system",40), fg="black", text="Last Initial")
    fnLabel = tk.Label(root,bg="white", font=("system",40), fg="black", text="First Initial:")
    cLabel = tk.Label(root,bg="white", font=("system",40), fg="black", text="Card Number:")

    lnLabel.grid(row=len(items) + 1, column=0,sticky='e')
    fnLabel.grid(row=len(items) + 2, column=0,sticky='e')
    cLabel.grid(row=len(items) + 3, column=0, sticky='e')

    # Entry fields
    lnField = tk.Entry(root,bg="white", font=("system",40), fg="black", textvariable=lName)
    fnField = tk.Entry(root,bg="white", font=("system",40), fg="black", textvariable=fName)
    cField = tk.Entry(root,bg="white", font=("system",40), fg="black", textvariable=card)

    lnField.bind("<FocusIn>", lambda event: on_field_select(entry =lnField))
    fnField.bind("<FocusIn>", lambda event: on_field_select(entry =fnField))
    cField.bind("<FocusIn>", lambda event: on_field_select(entry =cField))

    lnField.grid(row=len(items) + 1, column=1,columnspan=6)
    fnField.grid(row=len(items) + 2, column=1,columnspan=6)
    cField.grid(row=len(items) + 3, column=1, columnspan=6)

    selectedField = None
    # Checkout button 
    checkoutButton = tk.Button(root, text="Checkout",bg="white", font=("system",20), fg="black", command= lambda t = total :check(t))
    checkoutButton.grid(row=len(items) + 4, column=0, columnspan=2, pady=10)


    root.mainloop()