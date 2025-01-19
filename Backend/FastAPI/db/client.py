from pymongo import MongoClient

# Data base (local)
# db_client = MongoClient().local 

# Data base (remote)
db_client = MongoClient("mongodb+srv://test:test@usersdb.dqc69.mongodb.net/?retryWrites=true&w=majority&appName=UsersDB").test
