import tkinter as tk
from transact import query
from tkinter import messagebox
import uuid
def promptPurchase(meat, transNum):
    meat = (query("specMeat", [meat[0]]))[0]
    print(meat)
    
    _weight = tk.IntVar() #num of lbs of {meat} user wants to buy
    _weight.set(0)
    def setWeight(isAdding): #when add/subtract button clicked, updates _weight var
        if isAdding:
            _weight.set(_weight.get() +1)
        else:
            if _weight.get() > 0:
                _weight.set(_weight.get() -1)
        w = _weight.get()
        EnterLbs.config(text="{}".format(w)) #change the label's text for user's ease 
        
    def submit():
        weight = _weight.get()
        if meat[2] < weight:  # if they tried to add more meat than in stock, don't let them
            messagebox.showerror("Error", "Not enough stock available.")
        else:  # if adding to cart is feasible, add meat/type to cart table
            try:
                cart = uuid.uuid4()
                query("addToCart", [str(cart),transNum,meat[0],weight, None, "2"])
                root.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))  # Display SQL error message

    def leave(): #if doesnt want to add, simply destroy the popup
        root.destroy()

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Welcome to the Butcher Shop")
    root.configure(background="white")
    root.attributes('-fullscreen',True)

    QuestionPrompt = tk.Label(root,bg="white", font=("system",50), fg="black", text="How many lbs of {} do you want to purchase?".format(meat[0])) #remind them what meat theyre buying
    lbsLeftNote = tk.Label(root, bg="white",font=("system",50), fg="black",text="By the way, we only have {} lbs .".format(meat[2])) #let them know how much is left

    subtButton = tk.Button(root, text="-", font=("system",20),bg="black", fg="white",command=lambda:setWeight(0)) #to indicate number of pounds they wanna purchase
    EnterLbs = tk.Label(root, bg="white",font=("system",75),text="0")
    addButton = tk.Button(root, text="+",bg="black", font=("system",20),fg="white", command=lambda:setWeight(1))

    AddToCart= tk.Button(root, text="Add to cart",bg="green",fg="white",font=("system",20), command=lambda:submit())
    Cancel = tk.Button(root, text="Cancel", bg="red", fg="white",font=("system",20),command= lambda:leave())
    
    QuestionPrompt.pack(side="top", fill="y", expand=True)
    lbsLeftNote.pack(side="top", fill="y", expand=True)
    subtButton.pack(side="left", fill="x", expand=True)
    addButton.pack(side="right", fill="x", expand=True)
    EnterLbs.pack(side="top", fill="both", expand=True)
    Cancel.pack(side="left", fill="y", expand=True)
    AddToCart.pack(side="right", fill="y", expand=True)


    root.mainloop()
