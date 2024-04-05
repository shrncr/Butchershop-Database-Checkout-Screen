import tkinter as tk
def promptPurchase(meat):
    #helper function
    _weight = tk.IntVar()
    _weight.set(0)
    def setWeight(isAdding):
        if isAdding:
            _weight.set(_weight.get() +1)
        else:
            _weight.set(_weight.get() -1)
        EnterLbs.text = _weight.get()
        
    def submit():
        weight = _weight.get()
        _weight.set(0)
        root.destroy()
    def leave():
        root.destroy()
    root = tk.Tk()
    root.title("Welcome to the Butcher Shop")

    QuestionPrompt = tk.Label(root, text="How many lbs of {} do you want to purchase?".format(meat[0]))
    lbsLeftNote = tk.Label(root, text="By the way, we only have {} lbs .".format(meat[2]))

    subtButton = tk.Button(root, text="-", command=lambda:setWeight(0))
    EnterLbs = tk.Label(root, text=_weight.get(), textvariable=_weight)
    addButton = tk.Button(root, text="+", command=lambda:setWeight(1))

    AddToCart= tk.Button(root, text="Add to cart", command=lambda:submit())
    Cancel = tk.Button(root, text="Cancel", command= lambda:leave())
    
    QuestionPrompt.pack(pady=10)
    lbsLeftNote.pack(pady=10)
    subtButton.pack()
    addButton.pack()
    EnterLbs.pack()
    Cancel.pack()
    AddToCart.pack()


    root.mainloop()
