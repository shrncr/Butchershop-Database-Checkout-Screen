import tkinter as tk
import purchasePromptGUI 
from checkoutGUI import Checkout
from transact import query
import uuid
transNum = uuid.uuid4() #To identify whose items are in whose cart
def askWeight(type): #brings up promptPurchase gui for selected meat

    print(str(transNum) + "promptpur")
    purchasePromptGUI.promptPurchase(type, str(transNum))
    

def checkout():
    global transNum
    curT = transNum
    transNum = uuid.uuid1() #new transaction num, whether they purchase or not

    Checkout(str(curT)) #checking out
    
    
    



root = tk.Tk()
root.geometry("800x600")
root.title("Welcome to the Butcher Shop")
root.configure(background="white")
root.attributes('-fullscreen',True)
# Create a label widget
label = tk.Label(root,bg="white", font=("system",80), fg="black", text="Welcome to the Butcher Shop")
label.pack(side="top", fill="both",expand=True,pady=10)

meats=query("getMeat")#get meats available rn

#make purchase buttons for EACH meat which is currently available
for meat in meats:
    print(meat["typeOfMeat"])
    button= tk.Button(root,bg="white", font=("system",20), fg="black", text=meat["typeOfMeat"], command=lambda i=meat:askWeight(i))
    button.pack(side="top", fill="both",expand=True,pady=8)

    
button = tk.Button(root,bg="green", font=("system",20), fg="black", text="Purchase", command=checkout) #button to checkout
button.pack(side="bottom", fill="y",pady=50)

# Run the main event loop
root.mainloop()
