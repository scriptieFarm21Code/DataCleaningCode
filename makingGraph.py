
import pandas as pd
import sys
from pymongo import MongoClient
import matplotlib.pyplot as plt


client = MongoClient('mongodb://localhost:27017/')

db = client.weatherDataFarm21

allData = db.readingDataRaw.find({})


def getAllSensorId():
    sensorids = []
    for reading in allData:
        sensorids.append(reading['sensorId'])
        pass
    return list(dict.fromkeys(sensorids))
    pass

# Code
# Todo: Add Data
# Make overview of all types


def plotOneByOne():
    for sensorid in getAllSensorId():
        # Get the Data
        sensorData = pd.DataFrame(db.readingDataRaw.find({'sensorId': sensorid}).sort('orginalReadingId', 1))
        sensorData['timestampReading'] = pd.to_datetime(sensorData['timestampReading'])
        sensorData['date'] = sensorData['timestampReading'].dt.date

        plt.title(f'All Soil Moisture Sensor {sensorid}')
        plt.ylabel('Percentage')
        plt.xlabel('Dates')
        plt.grid(True)
        plt.autoscale(axis='x', tight=False)
        plt.plot(sensorData['soil_moisture_10'], label="soil 10")
        plt.plot(sensorData['soil_moisture_20'], label="soil 20")
        plt.plot(sensorData['soil_moisture_30'], label="soil 30")
        # plt.plot(sensorData['sensorHumidity'], label="Humidity")
        test = int(sensorData.shape[0] / 10)
        plt.xticks(range(0, sensorData.shape[0], test), sensorData['date'][::test], rotation=45)
        plt.subplots_adjust(bottom=0.2)
        plt.autoscale()
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper right', borderaxespad=0.)
        plt.rcParams["figure.figsize"] = (20, 7)
        plt.show()
    pass


def plotAll(allData):
    allData = pd.DataFrame(allData)
    print(allData)
    plt.title('All data prediction')
    plt.ylabel('Percentage')
    plt.xlabel('Dates')
    plt.grid(True)
    plt.autoscale(axis='x', tight=False)
    plt.plot(allData['soil_moisture_10'], label="soil 10")
    plt.plot(allData['soil_moisture_20'], label="soil 20")
    plt.plot(allData['soil_moisture_30'], label="soil 30")
    # plt.subplot(allData['timestampReading'])
    plt.autoscale()
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper right', borderaxespad=0.)
    plt.show()
    pass


def changeValues():
    df = pd.DataFrame(db.readingDataRaw.find({}))

    df.loc[df.humidity <= 1, 'humidity':] *= 100

    print(df.head)
    pass


changeValues()
