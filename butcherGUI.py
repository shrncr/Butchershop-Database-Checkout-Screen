import tkinter as tk
import mysql.connector
import purchasePromptGUI 

#connect to already existing butchershop
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Kiki1979!",
    database = "BUTCHERSHOP"
)
cursor = mydb.cursor()

#Grab all meat names and costs for meats which are currently in the shop
cursor.execute("SELECT typeOfMeat,pricePerPound,lbsRemaining from Meat WHERE lbsRemaining>0")
meats = cursor.fetchall()

def askWeight(type):
    purchasePromptGUI.promptPurchase(type)
    
def checkout():
    pass

root = tk.Tk()
root.title("Welcome to the Butcher Shop")

# Create a label widget
label = tk.Label(root, text="Welcome to the Butcher Shop")
label.pack(pady=10)

#make purchase buttons for EACH meat which is currently available
for meat in meats:
    button= tk.Button(root, text=meat[0], command=lambda:askWeight(meat))
    button.pack(pady=5)

button = tk.Button(root, text="Purchase", command=checkout) #button to buy
button.pack(pady=5)

# Run the main event loop
root.mainloop()
