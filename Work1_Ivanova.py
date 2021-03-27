from openpyxl import load_workbook
import geojson
import random


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


