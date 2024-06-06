# models 

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')


db = client['riding-shiring']

riders_collection = db['riders']
drivers_collection = db['drivers'] 
riders_collection = db['riders']

def create_indexes():
	riders_collection.create_index('riderId', unique=True) 
	drivers_collection.create_index('driverId', unique=True)

create_indexes()


