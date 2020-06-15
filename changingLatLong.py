

import pandas as pd
import sys
from pymongo import MongoClient
import mysql.connector
import matplotlib.pyplot as plt


client = MongoClient('mongodb://localhost:27017/')

farm21DB = mysql.connector.connect(
    host="127.0.0.1",
    user="homestead",
    password="secret",
    database="homestead"
)

cursor = farm21DB.cursor(dictionary=True, buffered=True)
db = client.weatherDataFarm21

allData = db.readingDataRaw.find({})
for reading in allData:
    cursor.execute(f"SELECT soil_type_id FROM sensors WHERE id = {reading['sensorId']}")
    result = cursor.fetchall()
    print(result)  # Print lenght to see if its enough

    print(reading['readingId'])

    db.readingDataRaw.update_one({'readingId': reading['readingId']}, {'$set': {'soilTypeId': result[0]['soil_type_id']}})

    # db.readingDataRaw.remove({' lat': float(result[0]['latitude'])})

    pass
