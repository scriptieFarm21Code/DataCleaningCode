

import pandas as pd
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

db = client.predictions

allData = db.tenRawPredictionNNGaussianFilter.find({})

for testingData in allData:

    calculatedTen = ((3477 - testingData['soil_ten_raw']) / 679) * 100

    testingData['calculatedTen'] = calculatedTen

    db.tenRawPredictionNNGaussianFilterCalculated.insert(testingData)
    pass
