'''
Queries associated w the butchershop
'''
import mysql.connector
def query(type, data=None): #data param only input if it is update/insert     
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Kiki1979!",
        database = "BUTCHERSHOP"
    )
    cursor = mydb.cursor()

    if type=="getMeat": #get available meat in the butchershop
        cursor.execute("SELECT typeOfMeat,pricePerPound,lbsRemaining from Meat WHERE lbsRemaining>0")
        meats = cursor.fetchall()
        return meats
    elif type == "addToCart": #adds entry to cart table when user taps "sumbit" button in purchasePromptGUI
        sql = "INSERT INTO cart (transactionID, typeOfMeat, weight) VALUES (%s, %s, %s)"
        val = (data[0], data[1], data[2])
        cursor.execute(sql, val)
        mydb.commit()
        
    elif type=="purchase": #adds to purchase table when a user fully checks out in checkoutGUI
        sql = "INSERT INTO Payment (purchaseID, lastFourDigits, lastNameOnCard, total) VALUES (%d, %s, %s, %d)"
        val = (data[0], data[1], data[2], data[3])
        mycursor.execute(sql, val)
        sql = "UPDATE Meat SET lbsRemaining=lbsRemaining-{} WHERE typeOfMeat ={}".format(lbsTaken, data[0]) #decreases meats by #lbs purchased
        #note: doesnt work bc it will have to decrease each meat which was purchased
        #probs have to use a for loop to make sure we get rid of each meat. idk. we have a whole week left to do this.

        mydb.commit()
    elif type=="getCart":#gets items you added to the cart just now
        cursor.execute("SELECT * FROM cart WHERE transactionID LIKE %s", ([data + "%"]))
        cart = cursor.fetchall()
        newList = []
        for item in cart:
            cursor.execute("SELECT pricePerPound FROM Meat WHERE typeOfMeat = %s", ([item[1]])) #we have to figure out how much money worth of each meat was added
            costs = cursor.fetchall() #price per pound
            print(int(item[2]))
            print(int(costs[0][0]))
            total = int(costs[0][0])*int(item[2]) #total aka p/lbXpounds
            newEntry = [item, total] #an array containing 2 elements: the original tuple, and the total cost of this cart item. sigh.
             #turn into tuple
            newList.append(newEntry)
        return newList
    

