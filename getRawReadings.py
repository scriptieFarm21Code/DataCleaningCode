import pandas as pd
import sys
import mysql.connector
from pymongo import MongoClient
import matplotlib.pyplot as plt

farm21DB = mysql.connector.connect(
    host="127.0.0.1",
    user="homestead",
    password="secret",
    database="homestead"
)

cursor = farm21DB.cursor(dictionary=True, buffered=True)
client = MongoClient('mongodb://localhost:27017/')
db = client.weatherDataFarm21

allData = db.trainDataFarm21.find({})

# Get original reading and update with other raw values
for reading in allData:

    cursor.execute(
        f"SELECT raw.soil_moisture_10, raw.soil_moisture_20, raw.soil_moisture_30 FROM readings JOIN raw_readings AS raw ON readings.raw_reading_id = raw.id WHERE readings.id = {reading['readingId']}")

    result = cursor.fetchall()

    reading['soil_moisture_10_raw'] = result[0]['soil_moisture_10']
    reading['soil_moisture_20_raw'] = result[0]['soil_moisture_20']
    reading['soil_moisture_30_raw'] = result[0]['soil_moisture_30']

    print(reading)
    db.trainDataRaw.insert(reading)
    pass
