from pymongo import MongoClient

def connect_mongo():
    client = MongoClient("mongodb://localhost:27017/")  
    db = client.BUTCHERSHOP  
    return db

db = connect_mongo()

meat_data = {
    "typeOfMeat": "Beef",
    "pricePerPound": 5,
    "lbsRemaining": 100
}

db.Meat.insert_one(meat_data) 
