import tkinter as tk
import mysql.connector
import purchasePromptGUI 
from checkoutGUI import Checkout
from transact import query
import uuid

transNum = uuid.uuid4() #To identify whose items are in whose cart
print(transNum)
def askWeight(type): #brings up promptPurchase gui for selected meat
    purchasePromptGUI.promptPurchase(type, str(transNum))
    
def checkout():
    Checkout(str(transNum))

root = tk.Tk()
root.title("Welcome to the Butcher Shop")

# Create a label widget
label = tk.Label(root, text="Welcome to the Butcher Shop")
label.pack(pady=10)

meats=query("getMeat")#get meats available rn

#make purchase buttons for EACH meat which is currently available
for meat in meats:
    button= tk.Button(root, text=meat[0], command=lambda:askWeight(meat))
    button.pack(pady=5)

button = tk.Button(root, text="Purchase", command=checkout) #button to checkout
button.pack(pady=5)

# Run the main event loop
root.mainloop()
