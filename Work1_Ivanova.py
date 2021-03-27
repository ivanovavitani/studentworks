from openpyxl import load_workbook
import geojson
import random
from pymongo import MongoClient


def opener():
    exl = load_workbook('data.xlsx')
    list = exl['Лист1']
    id = []
    x = []
    y = []
    for i in range(1,129):
        val = list.cell(row=i+1, column=1).value
        id.append(val)
    for i in range (1, 129):
        val = list.cell(row=i+1, column=2).value
        x.append(float(val))
    for i in range (1, 129):
        val = list.cell(row=i+1, column=3).value
        y.append(float(val))
    return id, x, y


id, x, y = opener()
coordinates = zip(y, x)
coordinates = list(coordinates)

features = []
for i in coordinates:
    width = [6, 10, 12]
    speed = [60, 80, 100, 120]
    type_of_surface = ["ground","city", "highway", "expressway"]
    lanes = [2, 4]
    features.append(geojson.Feature(geometry=geojson.Point(i), properties={"width":random.choice(width),
                                                                           "speed":random.choice(speed),
                                                                           "type of surface":random.choice(type_of_surface),
                                                                           "lanes":random.choice(lanes)}))
collection = geojson.FeatureCollection(features=features)

with open('Points.geojson', 'w') as file:
    geojson.dump(collection, file)
with open('Points_for_DB.json', 'w') as file:
    geojson.dump(features, file)

client = MongoClient('localhost', 27017)
db = client['MyDB']
collection_currency = db['MyColl']

#with open('Points_for_DB.json') as f:
    #file_data = geojson.load(f)
#collection_currency.insert_many(file_data)

# Это тестовая выборка из MongoDB
new_features = []
for i in collection_currency.find({'properties.speed': 100}):
    new_features.append(geojson.Feature(geometry=i['geometry'], properties=i['properties']))
new_feature_collection = geojson.FeatureCollection(features=new_features)

with open('Points#test.geojson', 'w') as r:
    geojson.dump(new_feature_collection, r)
