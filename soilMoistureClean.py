import sys
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.weatherDataFarm21

allReadings = db.trainDataNew.find({})
i = 0
for reading in allReadings:
    if(reading['soil_moisture_10'] > 100 or reading['soil_moisture_20'] > 100 or reading['soil_moisture_30'] > 100):
        i += 1
        print(reading)
        db.trainDataNew.remove({'orginalReadingId': reading['orginalReadingId']})
    pass
print(i)
