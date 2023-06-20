from pymongo import MongoClient
MONGO_URI = "mongodb+srv://PratikChavan:12345678pratik@cluster0.axzgan9.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client['register']
collection= db['users']


def addUser(newuser):
    result = db.collection.insert_one(newuser)
    return result