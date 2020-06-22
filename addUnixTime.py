from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')

db = client.weatherDataFarm21

allData = db.readingDataRaw.find({})


def convertTimeStap(timestamp):

    utc_time = datetime.strptime(str(timestamp), "%Y-%m-%d %H:%M:%S")

    return (utc_time - datetime(1970, 1, 1)).total_seconds()
    pass


for reading in allData:

    print(reading['readingId'])

    db.readingDataRaw.update_one({'readingId': reading['readingId']}, {'$set': {'unixTimestampReading': convertTimeStap(reading['timestampReading'])}})

    # db.readingDataRaw.remove({' lat': float(result[0]['latitude'])})

    pass
