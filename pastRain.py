import matplotlib.pyplot as plt
from pymongo import MongoClient
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


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

    return dataFrame


farm21DB = mysql.connector.connect(
    host="127.0.0.1",
    user="homestead",
    password="secret",
    database="homestead"
)

cursor = farm21DB.cursor(dictionary=True, buffered=True)

cursor.execute(f"SELECT readings.*, raw.weather_data FROM readings JOIN raw_readings as raw ON readings.raw_reading_id = raw.id WHERE raw.timestamp > 1587686400 AND raw.timestamp < 1588334400 AND readings.sensor_id = 100 AND raw.valid_reading = 1 AND readings.measured_at > 0 AND readings.soil_moisture_30 > 8 AND readings.latitude <> 0 AND readings.longitude <> 0 AND raw.weather_data IS NOT NULL AND readings.soil_moisture_10 <100 ORDER BY measured_at ASC")
result = cursor.fetchall()

print(result)

df = pd.DataFrame(result)

allData = getWeatherData(df)
allData = pd.to_numeric(allData)


print(allData)
print(allData.dtypes)


# print(allData)

plt.title(f'Tempratuur en Gevoelstempratuur')
plt.ylabel('Tempreatuur in Celsius')
plt.xlabel('Datum')
plt.grid(True)
plt.autoscale(axis='x', tight=False)
plt.plot(allData['temp'], label="Tempratuur")
plt.plot(allData['apparentTemperature'], label="Gevoelstemperatuur")
test = int(allData.shape[0] / 10)
plt.xticks(range(0,  allData.shape[0], test), allData['measured_at'][::test], rotation=45)
plt.subplots_adjust(bottom=0.2)
plt.autoscale()
plt.legend()
plt.rcParams["figure.figsize"] = (20, 7)
plt.show()


plt.title(f'Regenval')
plt.ylabel('Regenval in MM')
plt.xlabel('Datum')
plt.grid(True)
plt.autoscale(axis='x', tight=False)
plt.plot(allData['rain'], label="Regenval")
# plt.plot(allData['apparentTemperature'], label="Gevoels Temperatuur")
test = int(allData.shape[0] / 10)
plt.xticks(range(0,  allData.shape[0], test), allData['measured_at'][::test], rotation=45)
plt.subplots_adjust(bottom=0.2)
plt.autoscale()
plt.legend()
plt.rcParams["figure.figsize"] = (20, 7)
plt.show()


plt.title(f'Dauwpunt')
plt.ylabel('Dauwpunt')
plt.xlabel('Datum')
plt.grid(True)
plt.autoscale(axis='x', tight=False)
plt.plot(allData['dewPoint'], label="Dauwpunt")
# plt.plot(allData['apparentTemperature'], label="Gevoels Temperatuur")
test = int(allData.shape[0] / 10)
plt.xticks(range(0,  allData.shape[0], test), allData['measured_at'][::test], rotation=45)
plt.subplots_adjust(bottom=0.2)
plt.autoscale()
plt.legend()
plt.rcParams["figure.figsize"] = (20, 7)
plt.show()


plt.title(f'Luchtdruk')
plt.ylabel('Luchtdruk')
plt.xlabel('Datum')
plt.grid(True)
plt.autoscale(axis='x', tight=False)
plt.plot(allData['airPressure'], label="Luchtdruk")
# plt.plot(allData['apparentTemperature'], label="Gevoels Temperatuur")
test = int(allData.shape[0] / 10)
plt.xticks(range(0,  allData.shape[0], test), allData['measured_at'][::test], rotation=45)
plt.subplots_adjust(bottom=0.2)
plt.autoscale()
plt.legend()
plt.rcParams["figure.figsize"] = (20, 7)
plt.show()
