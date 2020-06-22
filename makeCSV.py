

import pandas as pd
import sys
from pymongo import MongoClient
import mysql.connector
import matplotlib.pyplot as plt


def makePDF(df):
    df.to_csv("./file.csv", sep=',', index=False)
    print(type(result))

    pass


def getWeatherData(dataFrame):
    # print(type(dataFrame))
    dataFrame['rain'] = dataFrame.weather_data.apply(lambda x: x.split(',')[0].split(':')[1].replace("'", "").replace("}", ""))
    dataFrame['temp'] = dataFrame.weather_data.apply(lambda x: x.split(',')[1].split(':')[1].replace("'", "").replace("}", ""))
    dataFrame['dewPoint'] = dataFrame.weather_data.apply(lambda x: x.split(',')[2].split(':')[1].replace("'", "").replace("}", ""))
    dataFrame['humidity'] = dataFrame.weather_data.apply(lambda x: x.split(',')[3].split(':')[1].replace("'", "").replace("}", ""))
    dataFrame['windSpeed'] = dataFrame.weather_data.apply(lambda x: x.split(',')[4].split(':')[1].replace("'", "").replace("}", ""))
    dataFrame['cloudCover'] = dataFrame.weather_data.apply(lambda x: x.split(',')[5].split(':')[1].replace("'", "").replace("}", ""))
    dataFrame['airPressure'] = dataFrame.weather_data.apply(lambda x: x.split(',')[6].split(':')[1].replace("'", "").replace("}", ""))
    dataFrame['windBearing'] = dataFrame.weather_data.apply(lambda x: x.split(',')[7].split(':')[1].replace("'", "").replace("}", ""))
    dataFrame['apparentTemperature'] = dataFrame.weather_data.apply(lambda x: x.split(',')[8].split(':')[1].replace("'", "").replace("}", ""))

    # dataFrame = dataFrame[~df.rain.str.contains('1h')]

    # print(dataFrame)

    dataFrame.drop(columns=['weather_data'], inplace=True)
    dataFrame.drop(columns=['measured_at'], inplace=True)
    dataFrame.drop(columns=['crop_type'], inplace=True)
    dataFrame.drop(columns=['race_type'], inplace=True)
    dataFrame.drop(columns=['cultivation_type'], inplace=True)
    dataFrame[~dataFrame.rain.str.contains("{")]
    print(dataFrame)

    dataFrame = dataFrame.astype(float)
    print(dataFrame)

    dataFrame.to_csv("./file.csv", sep=',', index=False)

    # for data in dataFrame['weather_data']:
    #     # print(type(data[]))
    #     pass
    pass


farm21DB = mysql.connector.connect(
    host="127.0.0.1",
    user="homestead",
    password="secret",
    database="homestead"


)

cursor = farm21DB.cursor(dictionary=True, buffered=True)

cursor.execute(f"SELECT readings.*, raw.timestamp, raw.timestamp ,raw.weather_data FROM readings JOIN raw_readings as raw ON readings.raw_reading_id = raw.id WHERE  raw.valid_reading = 1 AND readings.measured_at > 0 AND readings.soil_moisture_30 > 8 AND readings.latitude <> 0 AND readings.longitude <> 0 AND raw.weather_data IS NOT NULL AND readings.soil_moisture_10 <100 ORDER BY measured_at DESC")
result = cursor.fetchall()

df = pd.DataFrame(result)

makePDF(df)
